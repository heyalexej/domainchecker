#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import codecs
import csv
import json
import urllib2
from termcolor import colored

def read_keywords(filename):
    keywords = []
    with codecs.open(filename, "rU", "utf-16") as f:  # the standard exorts are utf-16. Use utf-8 if your work with your own files.
        reader = csv.reader(f, delimiter="\t")
        reader.next()  # skipping header
        for row in reader:
            keywords.append(row[1])
    return keywords


def domainr_info_json(domainname):
    requesturl = "http://www.domai.nr/api/json/info?q="
    requesturl += domainname
    request = urllib2.Request(requesturl)
    request.add_header("User-Agent", "domainchecker.py/0.1")
    opener = urllib2.build_opener()
    response = opener.open(request).read()
    objs = json.loads(response)
    return objs
    print domainname

def is_taken(domainr_json):
    return domainr_json["availability"] == "taken"


def concatenation(keyword, symbol):
    return symbol.join(keyword.split())
    print ("This: " + keyword)

def fetch_status(keywords):
    rows = [["Keyword", "com", "net", "org", "com hyphen", "net hyphen", "org hyphen"]]

    for keyword in keywords:
        row = [keyword]
        for symbol in ["", "-"]:
            for tld in [".com", ".net", ".org"]:
                domain = concatenation(keyword, symbol) + tld

                req = domainr_info_json(domain)
                if is_taken(req):
                    row.append(domain)
                    print colored("------- Domain Taken---------- : " + domain, 'magenta')
                else:
                    row.append("XXXXX")
                    print colored("------- Domain Free ---------- : " + domain, 'green')
        rows.append(row)

    return rows

def write_result(filename, rows):
    with open(filename, "wb") as res:
        writer = csv.writer(res, delimiter="\t")
        writer.writerows(rows)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="domainchecker", version="0.1")
    parser.add_argument("--input", "-i", type=str)
    parser.add_argument("--output", "-o", type=str)

    args = parser.parse_args()

    keywords = read_keywords(args.input)

    write_result(args.output, fetch_status(keywords))
