from math import sqrt

def compare(x,y):
    if (x>y):
        return 1
    elif (x==y):
        return 0
    else:
        return -1
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
def area(radius):
    return math.pi * radius**2

def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x

def distance(x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2
    ds_sqared=dx**2+dy**2
    result = sqrt(ds_sqared)
    return result

def hypotenuse(a,b):
    return sqrt(a**2+b**2)

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def is_between(x, y, z):
    if ((x <= y) and (y<=z)):
        return True
    else:
        return False

def factorial(n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None
    elif n == 0:
        return 1
    else:
        return(n*factorial(n-1))

def fibonacci (n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print "Compare 3,4:", compare(3,4)
print "Compare 4,3:", compare(4,3)
print "Compare 3,3:", compare(3,3)

print "Distance:", distance(1,2,4,6)
print "Hypotense:", hypotenuse(3,4)
print "isBetween:", is_between(3,4,5).__str__()
print "isBetween:", is_between(3,4,2).__str__()
print "isBetween:", is_between(3,7,5).__str__()
print "factorial 3:", factorial(3)
print "Fibonacci: "
for i in range(0,10):
    print fibonacci(i),