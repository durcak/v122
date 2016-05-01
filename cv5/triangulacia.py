from math import sqrt
from prieniky import intersection
import random
import svgwrite


size = 200

def draw(lines, points):
    img = svgwrite.Drawing('triangulacia.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')
    for k, l in lines:
        img.add(img.line(k, l, stroke=stroke))

    for p in points:
        img.add(img.circle(p, r = 3))

    img.save()

def intersection2(l1, l2):				#checks intersection of 2 lines
    ((x1, y1), (x2, y2)) = l1
    ((x3, y3), (x4, y4)) = l2

    if x1 == x3 and y1 == y3 \				#checks exists connections of lines
       or x2 == x3 and y2 == y3 \
       or x1 == x4 and y1 == y4 \
       or x2 == x4 and y2 == y4:
        return None
    else:
    	return intersection(l1,l2)


def intersection_lines(l1, lines):
    for l2 in lines:
        if intersection2(l1, l2) is not None:
            return True

    return False

def triangulate(points): 				# Greedy algorithm
    potentlines = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            potentlines.append((points[i], points[j]))  # generujeme vsetky kombinacie useciek
    potentlines.sort(key=length)			# usecky zoradi podla dlzky

    lines = []
    for l1 in potentlines:
        if not intersection_lines(l1, lines):
            lines.append(l1)

    return lines

def rand_point_generator():				# generator bodov
    x = random.randint(0, size-5)
    y = random.randint(0, size-5)
    return x,y

def length(l):
    (x1, y1), (x2, y2) = l
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

points = [rand_point_generator() for _ in range(100)]
lines = triangulate(points)
draw(lines, points)

