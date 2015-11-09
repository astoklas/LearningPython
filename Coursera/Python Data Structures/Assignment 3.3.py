def scoreing(myscore):
    if myscore >= 0.9:
        return "A"
    elif myscore >= 0.8:
        return "B"
    elif myscore >= 0.7:
        return "C"
    elif myscore >= 0.6:
        return "D"
    else:
        return "F"


try:
    score = float(raw_input("Score:"))
    if score >= 0.0 and score <= 1.0:
        print scoreing(score)
    else:
        print "Error, Score shall be in between 0.0 and 1.0"
        exit(1)

except ValueError:
    print "Floating Point Value expected"
    exit(1)
