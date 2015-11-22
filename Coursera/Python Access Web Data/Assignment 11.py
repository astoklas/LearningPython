import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_185051.txt"
handle = open(name)
mySum = 0

for line in handle:
    mySum = mySum + sum(map(int,re.findall('[0-9]+',line)))

print "Sum of Values:", mySum
