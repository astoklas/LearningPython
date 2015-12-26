import json
import urllib

sum = 0
address1 = 'http://python-data.dr-chuck.net/comments_42.json'
address2 = 'http://python-data.dr-chuck.net/comments_185057.json'

address = raw_input('Enter location: ')
if len(address) < 1 :
    url = address2
else:
    url = address

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try:
    info = json.loads(data)
except:
    exit(1)

count = len(info['comments'])
for item in info['comments']:

    sum = sum + int(item['count'])

print "Count: ", count
print "Sum :", sum
