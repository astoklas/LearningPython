__author__ = 'astoklas'

import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    BOLDBLUE = BOLD + OKBLUE
    BOLDGREEN = BOLD + OKGREEN


for j in range(1,200):
    liste = ""
    a = ["R","B"]
    countR = 0
    countB = 0
    for i in range(1,61):
        r = random.randint(0,i)
        value = a[r]
        if value == "R":
            a.append("R")
            liste += "R"
        else:
            a.append("B")
            liste += "B"
    for c in liste:
        if c == "R":
            print bcolors.FAIL + "R",
            countR += 1
        else:
            print bcolors.OKBLUE + "B",
            countB += 1
    print "  R:"+str(countR)+"  B:"+str(countB)


