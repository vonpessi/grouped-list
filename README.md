# grouped-list
grouped-list is a simple project where I practised a grouping URLs with Python.
## Getting started
Clone or download this repository
```
git clone https://github.com/vonpessi/grouped-list.git
```
### Prerequisites

#### 1. List of URLs. 

In this example I used a https://www.randomlists.com/ website to generate 100 random URLs and saved these on example_list_of_urls.txt. (example_list_of_urls.txt comes with this repository)

#### 2. Csv list of regular expressions and names.

This is an example of my regex.csv file. First column indicate a regular expression pattern and second column indicate a name of that regular expression. for example in first row ```b.*ket,basket```where ```b.*ket``` is regular expression and ```basket``` is a name.
```
b.*ket,basket
com,com
e.*ple,   < ------------- This one is without a name but there must be a comma after regular expression.
net,netti
af.*on,someNiceColumnName
```
If the name of that regular expression are not set like in third row```e.*ple,   ```. It's going to use a regular expression itself as a name. You can see that in step 3.

#### 3. Empty csv file for the saved data.

|Date|Url|basket|com|e.*ple|netti|esimerkki|
|---|---|---|---|---|---|---|
|2019-10-27 16:21:33.827716|https://www.example.com/?action=branch&attack=animal|False|True|True|False|False|

This script use a boolean value to indicate a match of a regular expression.


### How to use
Open your terminal and go to the grouped-list folder.
run python script as usual but you need to add three argument.

Order of arguments and explanations:
```
file1 = List of URLs
file2 = csv file of regular expressions and names
file3 = csv file where you you want to store the data
```
For example:
```
python3 grouplisting.py file1 file2 file3
```
In my case:
```
python3 grouplisting.py example_list_of_urls.txt regex.csv data/grouptest.csv
```
![alt text](https://github.com/vonpessi/grouped-list/blob/master/screenshot.png)
## How it works
This script should group URLs in 3 precongfigured groups and save it to data folder.

for example:

Directory
```
  http://www.example.com/basket/
  ```
Filename
```
  http://www.example.com/bomb/basket.php
  ```
Query
```
  https://boot.example.net/authority?basketball=airplane
```
At the moment regular expressions doesn't work perfectly.
