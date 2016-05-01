from PIL import Image
from math import sqrt, floor, ceil

width = 800
height = round(width * sqrt(3)/2)
img = Image.new('RGB', (width, int(height)), 'white')

def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum),float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    r = int(max(0, 255*(1 - ratio)))
    b = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b

for x in range(-width//2, width//2):
    y0 = floor(sqrt(3) * abs(x))
    for y in range(int(y0), int(height)):
	img.putpixel((int(x) + width//2, int(y) ), (rgb(x*height, abs(x)*width+15, x*y)))

img.save('img/triangle.png')
