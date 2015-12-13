# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

print "Assignment 12.2"

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))
if len(url) < 5:
    url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Izabel.html"
    #url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"

for i in range(count):

    print "Retreiving: ",url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
    tags = soup("a")
    url  = tags[pos-1].get('href', None)

print "Last Url: ", url
