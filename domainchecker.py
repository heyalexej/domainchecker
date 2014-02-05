#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import codecs
import csv
import json
import urllib2
from termcolor import colored


def bad_keyword(keyword):
    chars = set('.,\'&/$%@#')
    if any((c in chars) for c in keyword):
        return True
    else:
        return False


def read_keywords(filename):
    keywords = []

    ignored = open('ignored.txt', 'a')

    with codecs.open(filename, 'rU', 'utf-16') as f:
#    with codecs.open(filename, 'rU', 'utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        reader.next()  # skipping header
        for row in reader:
            keyword = row[1]
            if not bad_keyword(keyword):
                keywords.append(row[1])
            else:
                ignored.write(keyword)
                ignored.write('\n')

        ignored.close()

        return keywords


def domainr_info_json(domainname):
    requesturl = 'http://www.domai.nr/api/json/info?q='
    requesturl += domainname
    request = urllib2.Request(requesturl)
    request.add_header(
        'User-Agent', 'Mozilla/2.0 (compatible; MSIE 3.0; Windows 95)'
    )
    opener = urllib2.build_opener()
    response = opener.open(request).read()
    objs = json.loads(response)
    return objs


def is_taken(domainr_json):
    return domainr_json['availability'] == 'taken'


def concatenation(keyword, symbol):
    return symbol.join(keyword.split())


def prepare_keywords(keyword):
    keywords = []
    if ' ' in keyword:
        for symbol in ['', '-']:
            keywords.append(concatenation(keyword, symbol))
    else:
        keywords.append(keyword)
    return keywords


def fetch_single(domain, row):
    try:
        req = domainr_info_json(domain)
    except Exception as e:
        print(colored('Error "{0}" occurred when requesting '
                      '{1} domain'.format(e, domain), 'red'))
        return

    if is_taken(req):
        print(colored('Domain Taken --------- : {0}'.format(domain), 'red'))
        row.append(domain)
    else:
        print(colored('Domain Free ---------- : {0}'.format(domain), 'green'))
        row.append('XXXXX')


def fetch_status(keywords):
    rows = [['Keyword', 'com', 'net', 'org', 'com hyphen', 'net hyphen', 'org hyphen']]

    for keyword in keywords:
        is_singlekey = ' ' not in keyword
        keyword = keyword.lower()
        row = [keyword]
        for keyword in prepare_keywords(keyword):
            for tld in ['.com', '.net', '.org']:
                fetch_single('{0}{1}'.format(keyword, tld), row)
        if is_singlekey:
            row += ['XXXXX']*3

        rows.append(row)
    return rows


def write_result(filename, rows):
    with open(filename, 'wb') as res:
        writer = csv.writer(res, delimiter='\t')
        writer.writerows(rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='domainchecker', version='0.3')
    parser.add_argument('--input', '-i', type=str)
    parser.add_argument('--output', '-o', type=str)

    args = parser.parse_args()

    keywords = read_keywords(args.input)

    write_result(args.output, fetch_status(keywords))
