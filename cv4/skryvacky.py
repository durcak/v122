from PIL import Image

def seek_one():
    img = Image.open('skryvacka1.png')
    pixels = img.load()

    for i in range(0,img.size[0]):
	for j in range(0,img.size[1]):
    	    r,g,b,a = pixels[i,j]
	    if b == 0:
	       pixels[i,j] = (0,0,0)

    img.save('img/sk1.png')


seek_one()

def seek_two():
    img = Image.open('skryvacka2.png')
    pixels   = img.load()
    for y in xrange(img.size[1]-1):
        for x in xrange(img.size[0]-1):
            if  abs(pixels[x, y][0] - pixels[x + 1, y][0]) > 3:
                pixels[x,y] = (255,255,255)

    img.save("img/sk2.png")

seek_two() 


def seek_three():
    img = Image.open('skryvacka3.png')
    pixels = img.load()

    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            if i % 2 or j % 2:
               r,g,b,a = pixels[i,j]
               pixels[i,j] = (255,255,255)

    img.save('img/sk3.png')

seek_three()


