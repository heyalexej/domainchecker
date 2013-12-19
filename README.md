#Domain Checker
 
Export keyword ideas from Google's Ad Planner and check for availability.
This command line tool goes through the second column of the exported CSV file and concatenates the keywords like so: `your keyword` becomes `yourkeyword` and `your-keyword`. 

The script then checks for domain availability like so: `yourkeyword.com`, `yourkeyword.net`, `yourkeyword.org`, `yourkeyword.info` and then the second class citizens of the interwebz `your-keyword.com`, `your-keyword.net`, `your-keyword.org`, `your-keyword.info` and writes the results to your specified output file.

##Usage

Run the script from your command line:

```bash
$ git clone git@github.com:heyalexej/domainchecker.git
$ pip install -r requirements.txt
$ python domainchecker.py -i inputfile.csv -o outputfile.csv
```

Easy, ha?

###Todo

Add exception handling and write on error.


**License:** [Do whatever the fuck you want!](http://www.wtfpl.net)