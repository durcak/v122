from PIL     import Image
from math    import pi, tan, sqrt, cos,sin

def spiral(size=600, path="img/spiral.png"):

    img = Image.new('RGB', (size,size), 'white')
    for length in xrange(0,size*25):
        angle = (length * pi) / 180
	#angle = length * 0.5 zemni obrazok na nieco ako kvet
    	x     = (1 + angle)*cos(angle)
    	y     = (1 + angle)*sin(angle)

        img.putpixel( (int(x) + size//2, int(y) + size//2), (length % 255,length % 13,length % 159))
    img.save(path)

spiral()
