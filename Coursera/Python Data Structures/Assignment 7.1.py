# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except IOError:
    print("File doesn't exist ")
    print(ValueError)
    exit(1)

for line in fh:
    print line.upper().strip()
