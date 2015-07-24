from math import sqrt
from math import pi


def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


def area(radius):
    return pi * radius ** 2


def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x


def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    ds_sqared = dx ** 2 + dy ** 2
    result = sqrt(ds_sqared)
    return result


def hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)


def circle_area(xc, yc, xp, yp):
    """

    :type xc: int
    """
    return area(distance(xc, yc, xp, yp))


def is_between(x, y, z):
    if (x <= y) and (y <= z):
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
        return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Exercise 6-5

def ack(m, n):
    if not isinstance(n, int) and not isinstance(m, int):
        print 'Error, n and m need to be of type int'
        return None
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        result = ack(m - 1, 1)
        return result
    if m > 0 and n > 0:
        result = ack(m - 1, ack(m, n - 1))
        return result


# Exercise 6-6

def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    f = first(word)
    l = last(word)
    m = middle(word)
    # print "first/last/middle",f,l,m
    if f == l:
        if len(m) > 0:
            return is_palindrome(m)
        elif len(m) <= 1:
            return True
        else:
            return False
    else:
        return False


def is_palindrome2(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome2(middle(word))


# Exercise 6-7
# A number, a, is a power of b if it is divisible by b and a/b is a power of b.
# Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
# Note: you will have to think about the base case.
# don't understand the algorithm
def is_power(a, b):
    return 0

# Exercise 6-8
def gdc(a, b):
    q = a / b
    r = a % b
    if r > 0:
        return gdc(b, r)
    else:
        return b


print "Compare 3,4:", compare(3, 4)
print "Compare 4,3:", compare(4, 3)
print "Compare 3,3:", compare(3, 3)

print "Distance:", distance(1, 2, 4, 6)
print "Hypotense:", hypotenuse(3, 4)
print "isBetween:", is_between(3, 4, 5).__str__()
print "isBetween:", is_between(3, 4, 2).__str__()
print "isBetween:", is_between(3, 7, 5).__str__()
print "factorial 3:", factorial(3)
print "Fibonacci: "
for i in range(0, 10):
    print fibonacci(i),
print ""
print "Ackermann 3,4 should be 125:", ack(3, 4)

print "is_palindrome otto", is_palindrome("otto").__str__(), is_palindrome2("otto").__str__()
print "is_palindrome noon", is_palindrome("noon").__str__(), is_palindrome2("noon").__str__()
print "is_palindrome redivider", is_palindrome("redivider").__str__(), is_palindrome2("redivider").__str__()
print "is_palindrome other", is_palindrome("other").__str__(), is_palindrome2("other").__str__()
print "is_palindrome 1234321", is_palindrome("1234321").__str__(), is_palindrome2("1234321").__str__()
print "is_palindrome 12344321", is_palindrome("12344321").__str__(), is_palindrome2("12344321").__str__()
print "is_palindrome 123444321", is_palindrome("123444321").__str__(), is_palindrome2("123444321").__str__()

print "GDC of 1071 and 462(should be 21): ", gdc(1071, 462)
print "GDC of 1071 and 462(should be 21): ", gdc(462, 1071)