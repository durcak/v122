import itertools
from PIL  import Image
from math import pi, sin, cos,sqrt


def mriezka(size=500):

    img = Image.new('RGB', (size,size))

    for x, y in itertools.product(xrange(size), xrange(size)):
        r = int( 255*abs(sin(x/10.)         ))
        g = int( 255*abs(sin(y/10.)         ))
        b = int( 255*abs(sin(x/10. + y/10.)))
        img.putpixel((x, y), (r, g, b))

    img.save("img/farebnamriezka.png")


def waves(A=400, a=200):

    img   = Image.new('RGB', (A,A), 'white')
    posun = A/2

    for x, y in itertools.product(xrange(-A/2, A/2), xrange(-A/2, A/2)):
        coef = abs( sin( sqrt((x/5.)**2 + (y/5.)**2) ))
        if abs(x) <= a/2 and abs(y) < a/2:
            coef = 1 - coef
        img.putpixel( (x + posun, y + posun), tuple([int(255 * coef)] * 4))

    img.save("img/waves_sin.png")

if __name__ == '__main__':
    waves()
    mriezka()
