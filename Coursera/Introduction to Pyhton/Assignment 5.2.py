largest = None
smallest = None
loop = True
while loop:
    numRaw = raw_input("Enter a number: ")
    try:
        num = int(numRaw)
        if num > largest:
            largest = num
            if smallest is None:
                smallest = largest
            print "largest: " , num
        if num < smallest:
            smallest = num
            print "smallest:" , num
    except ValueError:
        if numRaw == "done":
            loop = False
        else:
            print "Invalid input"

print "Maximum", largest
print "Minimum", smallest