from Turtle import Turtle
from math import sqrt, ceil, sin,tan,cos,pi


def squares(max_levels = 15):

	t = Turtle('squares')
	d = 300

	for i in range(max_levels):
	    for i in range(4):
		t.forward(d)
		t.right(90)

	    t.forward(d/4)
	    t.right(90/5)

	    d = sqrt((d/4)**2 + (d - d/4)**2)

	t.save()

def triangles(side=100, step=20, n=10):
	t = Turtle('triangles')
	d = 300

	for i in xrange(n):
		side += (3*step)

		t.polygon(3, side)
		t.right(120)
		t.pen_up()
		t.forward(step)
		t.left(120)
		t.back(step)
		t.pen_down()
	t.save()

def polycircle(n=12):
    t = Turtle('polycircle')

    for x in xrange(n):
        t.polygon(n, 20)
        t.left(360/n)
    t.save()

if __name__ == '__main__':
	squares()
	polycircle()
	triangles()
