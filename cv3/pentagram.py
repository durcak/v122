from Turtle import Turtle
import math

dist = 100
golden_ratio = (1 + 5 ** 0.5) / 2

turtle = Turtle('pentagram_rel')

turtle.right(90/5)

for i in range(5):
    turtle.right(360/5)
    turtle.forward(dist)

turtle.right(90 + 90/5)

for i in range(5):
    turtle.right((180 - (360/5)) / 3)
    if i % 2 == 0:
        turtle.forward(dist*golden_ratio)
    else:
        turtle.back(dist*golden_ratio)

turtle.save()

#################### pentagram absolute
import svgwrite
from math import sin,sqrt,tan,cos,pi

def render(lines):
    dwg = svgwrite.Drawing('pentagram_abs.svg', profile='tiny')
    stroke = svgwrite.rgb(10, 10, 16, '%')

    for f,t in lines:
        dwg.add(dwg.line(f, t, stroke=stroke))

    dwg.save()

###

p = [None for _ in range(5)]

p[0] = (-100+200, 0+200)
p[1] = (100+200, 0+200)
p[2] = (100 + 200*cos(72*pi/180)+200, 200*sin(72*pi/180)+200)
p[3] = (0+200, 100*tan(72*pi/180)+200)
p[4] = (-1*(100 + 200*cos(72*pi/180))+200, 200*sin(72*pi/180)+200)

lines = []

for i in range(5):
    f, t = p[i], p[(i + 1) % 5]
    lines.append((f,t))

for i in range(5):
    f, t = p[i], p[(i + 2) % 5]
    lines.append((f,t))

render(lines)
