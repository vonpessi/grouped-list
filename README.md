# grouped-list
grouped-list is a simple example where I practised a grouping URL's with Python.
## Getting started
Clone or download this repository
```
git clone https://github.com/vonpessi/grouped-list.git
```
### Prerequisites
```
List of URL's. 
```
In this example I used a https://www.randomlists.com/ website to generate 100 random URL's and saved these on example_list_of_urls.txt. (example_list_of_urls.txt comes with this repository)

### How to use
Open your terminal and go to the grouped-list folder.
run python script as usual but use some list of URL's as an argument.
```
python3 grouplisting.py <Here some list of URLS's>
```
In my example
```
python3 grouplisting.py example_list_of_urls.txt
```
![alt text](https://github.com/vonpessi/grouped-list/blob/master/screenshot.png)
## How it works
This script should group URL's in 3 precongfigured groups and save it to data folder.

for example:
```
Folder
  http://www.example.com/basket/
Filename
  http://www.example.com/bomb/basket.php
Query
  https://boot.example.net/authority?basketball=airplane
```
At the moment regular expressions doesn't work perfectly.
