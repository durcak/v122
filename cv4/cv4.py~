from PIL import Image
from math import sqrt

def circle(size=500, r=100, eps=10):
    img = Image.new('RGB', (size,size), 'white')
    pixels = img.load()

    for i in range(-size//2, size//2):
        for j in range(-size//2, size//2):
            x, y = i + size // 2, j + size // 2
            if size//2 - 2-5 <= sqrt(i*i + j*j) and sqrt(i*i + j*j) < size//2-5:
                pixels[x,y] = (0,0,0)

    img.show()
    img.save('circle.png')

def disk(size=500, r=100, eps=10):
    img = Image.new('RGB', (size,size), 'white')
    pixels = img.load()

    for i in range(-size//2, size//2):
        for j in range(-size//2, size//2):
            x, y = i + size // 2, j + size // 2
            if sqrt(i*i + j*j) < size//2-5:
                pixels[x,y] = (0,0,0)

    #img.show()
    img.save('disk.png')


def circle_par(size=500, r=100):
   img = Image.new('RGB', (size, size), 'white')
   for t in range(0,360):
       x = math.pi*r/180*(math.cos(t))
       y = math.pi*r/180*(math.sin(t))		
       img.putpixel((x,y),(0,0,0))
   #img.show()
   img.save('circle.png')



circle()
disk()
