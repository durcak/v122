import svgwrite
from math import sin, cos, pi
import random

size = 500

def render(lines, points):
    img = svgwrite.Drawing('intersections.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')
    for f, t in lines:
        img.add(img.line(f, t, stroke=stroke))

    for p in points:
        img.add(img.circle(p, r = 3))

    img.save()


def rand_lines_generator():

    x1 = random.randint(0 + 20, size - size/2)
    y1 = random.randint(0 + 20, size - size/2)

    x2 = random.randint(0 + 20, size - size/2)
    y2 = random.randint(0 + 20, size - size/2)

    return ((x1,y1),(x2,y2))

def intersection(line1, line2):

    ((x1, y1), (x2, y2)) = line1
    ((x3, y3), (x4, y4)) = line2

    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

    if denom == 0:	# When the two lines are parallel or coincident the denominator is zero.
        return None

    x = ( (x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4) ) / denom  # vzorec zo slaidov
    y = ( (x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4) ) / denom

    # kontrola kde sa nachadza prienik, pretoze vzorec hlada prieniky priamok nie useciek
    if   (x < min(x1, x2) or x > max(x1, x2)) or (y < min(y1, y2) or y > max(y1, y2))\
      or (x < min(x3, x4) or x > max(x3, x4)) or (y < min(y3, y4) or y > max(y3, y4)):		
        return None

    return x,y

def intersections_lines(lines):
    result = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            p = intersection(lines[i], lines[j])
            if p is not None:
                result.append(p)

    return result


lines = [rand_lines_generator() for _ in range(30)]
points = intersections_lines(lines)
render(lines, points)

