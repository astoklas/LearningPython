from swampy.TurtleWorld import *
from math import *

def square(turtle, length):
    for i in range(4):
        fd(turtle,length)
        lt(turtle)

# Kreissehne: s = 2r*sin(alpha/2)
# alpha im Bogenmass
# Umrechnung Grad in Bogenmass: rad=winkle*pi/180

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def n_eck(turtle,radius,edges):
    alpha = 360.0 / edges
    alpha_half_rad = alpha / 2.0 * pi / 180.0
    sin_alpha_half = sin(alpha_half_rad)
    s = 2.0*radius*sin_alpha_half
    lt(turtle,alpha/2)
    for i in range(edges):
        fd(turtle,s)
        lt(turtle,alpha)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

def koch(t, length):
    if length >= 3:
        koch(t,length/3)
        lt(t,60)
        koch(t,length/3)
        rt(t,120)
        koch(t,length/3)
        lt(t,60)
        koch(t,length/3)
    else:
        fd(t,length)

def snowflake(t, length):
    for i in range(3):
        koch(t,length)
        rt(t,120)


world = TurtleWorld()
#winkel = [3,4,5,6,7,8,9,12,24,36,48,96]
#for i in winkel:
#    print "Winkel i=",i
#    mal = Turtle()
#    mal.delay = 0.025
#    print mal
#    n_eck(mal,100,i)
#    mal.die()
#mal = Turtle()
#arc(mal,100,30)
#mal.die()


t = Turtle()
t.delay = 0.0
#draw(t,5,3)
snowflake(t,240)
t.die()
wait_for_user()