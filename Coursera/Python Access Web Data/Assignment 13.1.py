import urllib
import xml.etree.ElementTree as ET

address1 = 'http://python-data.dr-chuck.net/comments_42.xml'
address2 = 'http://python-data.dr-chuck.net/comments_185053.xml'
sum = 0
count = 0

address = raw_input('Enter location: ')
if len(address) < 1 :
    url = address2
else:
    url = address

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
root = ET.fromstring(data)

for element in root.iter('comment'):
    sum = sum + int(element.find('count').text)
    count = count + 1

print "Count: ", count
print "Sum: ", sum