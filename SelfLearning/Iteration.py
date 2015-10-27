__author__ = 'astoklas'

import math

def countdown(n):
    while n > 0:
        print n, "..",
        n -= 1
    print "Take Off"

def sequence(n):
    while n != 1:
        print n,",",
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1
    print n

def newton_sqrt(a, x):
    y = (x + a/x) / 2
    return y

def test_sqrt(n):
    for i in range(1,n+1,1):
        print i
        a = i
        x = 1.0
        y = 0.0
        while True:
            y = newton_sqrt(a,x)
            if abs(y-x) < epsilon:
                break
            else:
                x = y
    print "End"

#
# Exercise 7.3
# PI approximation
#

def estimatePi():
    term = 1.0
    sum_term = 0
    k = 0
    result = 2.0*math.sqrt(2.0)/9801.0
    while term>1e-15:
        term = math.factorial(4*k)*(1103+26390*k)/(math.pow(math.factorial(k),4)*math.pow(396,4*k))
        sum_term += term
        k += 1
    result *= sum_term
    return 1/result

countdown(2)
sequence(36766)
print "Newton SQRT"
x = 1.0
y = 0.0
a = 25
epsilon = 0.000000001

test_sqrt(5)
print "Estimate PI"
a = estimatePi()
print a
print math.pi
