from Turtle import Turtle
import math

turtle = Turtle('r_polygon')

n = 5
dist = 1000 / n

for i in range(n):
    turtle.right(360/n)
    turtle.forward(dist)

turtle.save()
