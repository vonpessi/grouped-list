# grouped-list
grouped-list is a simple project where I practised a grouping URLs with Python.
## Getting started
Clone or download this repository
```
git clone https://github.com/vonpessi/grouped-list.git
```
### Prerequisites
```
List of URLs. 
```
In this example I used a https://www.randomlists.com/ website to generate 100 random URLs and saved these on example_list_of_urls.txt. (example_list_of_urls.txt comes with this repository)

### How to use
Open your terminal and go to the grouped-list folder.
run python script as usual but use some list of URLs as an argument.

For example:
```
python3 grouplisting.py <Here some list of URLSs>
```
In my case:
```
python3 grouplisting.py example_list_of_urls.txt
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
