name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mailer = dict()

for line in handle:
    words = line.split(' ')
    if words[0].upper() == "FROM":
        if words[1] in mailer:
            mailer[words[1]] = mailer[words[1]] + 1
        else:
            mailer[words[1]] = 1
maxval = 0;
s = ""

for sender in mailer:
    if mailer[sender] > maxval:
        s = sender
        maxval = mailer[sender]

print s, maxval