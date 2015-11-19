name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

distribution = dict()

for line in handle:
    words = line.split(' ')
    if words[0].upper() == "FROM":
        hrs = words[6].split(':')[0]
        if hrs in distribution:
            distribution[hrs] = distribution[hrs] + 1
        else:
            distribution[hrs] = 1

for key, value in sorted(distribution.items()):
    print key, value