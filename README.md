# grouped-list
grouped-list is a simple project where I practised a grouping URLs with Python.
## Getting started
Clone or download this repository
```
git clone https://github.com/vonpessi/grouped-list.git
```
### Prerequisites
All the necessary files comes with this repository for testing purpose.
#### 1. List of URLs. 

In this example I used the following websites:
```
https://github.com/vonpessi/grouped-list
https://www.python.org/
```
and saved these on example_list_of_urls.txt. (example_list_of_urls.txt comes with this repository)

#### 2. Csv list of regular expressions and names.

This is an example of my regex.csv file. First column indicate a regular expression pattern and second column indicate a name of that regular expression. for example in first row ```b.*ket,basket```where ```b.*ket``` is regular expression and ```basket``` is a name.
```
`b.*ket,basket
vonpessi,pessi
branch,branch
e.*ple,< ------------- This one is without a name but there must be a comma after regular expression.
systeemi,netti
af.*on,esimerkki
```
If the name of that regular expression are not set like in third row```e.*ple,   ```. It's going to use a regular expression itself as a name.

#### 3. Empty csv file for the data.

### How to use
Open your terminal and go to the grouped-list folder.
run python script as usual but you need to add three argument.

Order of arguments and explanations:
```
file1 = List of URLs for example .txt file
file2 = csv file of regular expressions and names
file3 = csv file where you you want to store the data
```
For example:
```
python3 grouplisting.py file1 file2 file3
```
For testing run:
```
python3 grouplisting.py example_list_of_urls.txt regex.csv data/grouptest.csv
```
## How it works
This script check url list line by line. On each url, script going through whole regular expression list and if regEx match the url then it gives a boolean True value and save all of the data to .csv file.

for example:

From this URL:
```
https://www.example.com/?action=branch&attack=animal
```
and these regular expressions and names(check prerequisites step 2.):
```
vonpessi,pessi
branch,branch
e.*ple,
systeemi,netti
af.*on,esimerkki
```

There is a two first rows of this data/grouptest.csv file.

|Date|Url|pessi|branch|e.*ple|netti|esimerkki|
|---|---|---|---|---|---|---|
|2019-10-28 17:21:59.692304|https://github.com/vonpessi/grouped-list|True|True|True|False|True|

