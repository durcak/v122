import svgwrite
from PIL import Image

def count_star(side, n):	# side = length of side, n = devider

	step = side/n
	lines = []
	for i in range(n+1):
		x0 = 0
		x1 = side - step*i
		y0 = step*i
		y1 = 0
		lines.append([x0, y0, x1, y1])
		lines.append([x0, -y0, -x1, y1])
		lines.append([x0, y0, -x1, y1])
		lines.append([x0, -y0, x1, y1])
	return lines


def draw_star(side, n):

	im = svgwrite.drawing.Drawing()
	lines = count_star(side, n)

	for line in lines:
		A = (line[0]+side, line[1]+side)
		B = (line[2]+side, line[3]+side)
		im.add( im.line(start = A, end = B, stroke= 'black' ))
	im.saveas('star.svg')
	

def colour_square():

    img = Image.new( 'RGB', (255,255), (0,0,0))
    pixels = img.load()

    for i in xrange(img.size[0]):  
        for j in xrange(img.size[1]):
            pixels[i,j] = (i, 0, j) 
    img.save('colourSquare.bmp')


draw_star(200,15)
colour_square()
