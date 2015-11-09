# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
linecount = 0
value = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line
    linecount += 1
    value += float(line[line.find(':')+1:].strip())

#print "LineCount: "+linecount.__str__()
#print "Value: "+value.__str__()
average = value / linecount
print "Average spam confidence: %.12f"%(average)
#print "Done"
