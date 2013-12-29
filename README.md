Domain Checker
==============
 
Export keyword ideas from Google's Ad Planner and check for availability.
This command line tool goes through the second column of the exported CSV file and concatenates the keywords like so: `your keyword` becomes `yourkeyword` and `your-keyword`. 

The script then checks for domain availability like so: `yourkeyword.com`, `yourkeyword.net`, `yourkeyword.org`, `yourkeyword.info` and then the second class citizens of the interwebz `your-keyword.com`, `your-keyword.net`, `your-keyword.org`, `your-keyword.info` and writes the results to your specified output file.

If the list contains keywords with special chars like `&/$%@#` they get written to a file called `ignored.txt` and skipped by the script to avoid errors. That way you can manually review them and make further decisions.

The script should write to CSV even if it runs into an issue.

Why?
----
[![Geeks vs. Mortals](https://lh5.googleusercontent.com/59j9us2ZAhfDMY3uTu6tCrQz9WhFsVndtjKLz8RQSG0=w800-h570-no)](https://plus.google.com/+BrunoOliveira/posts/MGxauXypb1Y)


Usage
-----

Run the script from your command line:

```bash
$ git clone git@github.com:heyalexej/domainchecker.git
$ pip install -r requirements.txt
$ python domainchecker.py -i inputfile.csv -o outputfile.csv
```

Easy, ha?

Todo
----

- <del>Add exception handling</del>
- <del>Write on error</del>
- Add recognition of single keywords.

Known Issues
------------

- Sometimes 304 errors!? from API
- Sometimes false positives.



Author
------

**Twitter:** [@heyalexej](http://twitter.com/heyalexej)

**GitHub:** [github.com/heyalexej](https://github.com/heyalexej)


**License:** [Do whatever the fuck you want!](http://www.wtfpl.net)
