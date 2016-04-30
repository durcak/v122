from Turtle import Turtle
import math

turtl = Turtle('sierpinsky')

def sierpinsky(side, level):
    if level == 0:
        for a in [1,2,3]:
            turtl.forward(side)
            turtl.left(120)
    else:
        sierpinsky(side / 2, level - 1)
        turtl.forward(side/2)

        sierpinsky(side / 2, level - 1)
        for d in [side/2, side, side/2]:
            turtl.forward(d)
            turtl.left(120)

        sierpinsky(side / 2, level - 1)
        turtl.right(120)
        turtl.forward(side/2)
        turtl.left(120)

turtl.left(90)
sierpinsky(800, 5)

turtl.save()
