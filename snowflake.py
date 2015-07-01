__author__ = 'astoklas'

from swampy.TurtleWorld import *


def koch(t, length):
    if length >= 3:
        m = length / 3.0
        koch(t, m)
        lt(t, 60)
        koch(t, m)
        rt(t, 120)
        koch(t, m)
        lt(t, 60)
        koch(t, m)
    else:
        fd(t, length)


def snowflake(t, length):
    for i in range(3):
        koch(t, length)
        rt(t, 120)


def moveturtle(t, x, y, d):
    t.delay = d
    t.x = x
    t.y = y
    t.redraw()


world = TurtleWorld()
bob = Turtle()
moveturtle(bob, -150, 90, 0.0)
snowflake(bob, 320)
bob.die()
user = wait_for_user()
