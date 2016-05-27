import numpy as np
from math import sin, cos, pi, radians
import svgwrite


# afinne transformacie
def rotate(angle):
    #angle = angle / 180 * pi;
    return np.array([
        [cos(angle), -sin(angle), 0],
        [sin(angle),  cos(angle), 0],
        [0, 0, 1]
    ])

def scale(x, y):
    return np.array([
        [x, 0, 0],
        [0, y, 0],
        [0, 0, 1],
    ])

def translate(tx, ty):
    return np.array([
        [1,0,tx],
        [0,1,ty],
        [0,0,1]
    ])

def shear(k):
    return np.array([
        [1,k,0],
  	[0,1,0],
	[0,0,1]
    ])

def square(a=100):
    return np.array([
        [0,0,1],
        [0,a,1],
        [a,a,1],
        [a,0,1]
    ])

#pripravy trans. maticu vynasobenim vsetkych transformacii v liste translist
def trans(translist):
    A = np.identity(3)
    for B in translist:
        A = np.dot(A, B)
    return A

# transformuje priamku
def trans_vektor(vector, transf):
    x, y = vector
    tr = transf
    return (tr[0][0]*x + tr[0][1]*y + tr[0][2],
            tr[1][0]*x + tr[1][1]*y + tr[1][2])
 

#nejaka skusobna metoda
def ex1(name):
    stvorec = square(200)
    pocet_opakovani = 120
    translist = []

    translist.append(shear(0.1))
    translist.append(rotate(radians(7)))
   
    name = "pokus4"
    img = svgwrite.Drawing('transformations_' + name + '.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')    
    size = 1000
    
    for i in range(pocet_opakovani): 
        lines = []
        for bod in stvorec:
            lines.append(np.dot(trans(translist),[bod[0],bod[1],1]))
              
        #vykresleni jednu transformaciu  
        for idx,bod in enumerate(lines):
            bod2 = lines[(idx+1)%len(lines)]

            fr = ( int(bod[0]+size/2), int(bod[1])+size/2 )
 	    to = ( int(bod2[0]+size/2), int(bod2[1])+size/2 )
    
            img.add(img.line(fr, to, stroke=stroke))

        stvorec = lines
    img.save()

#vykresli utvar ulozeny v lines
def drawImage(lines, name):
    img = svgwrite.Drawing('transformations_' + name + '.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')    
    size = 1000

    for idx,bod in enumerate(lines):
        bod2 = lines[(idx+1)%len(lines)]
        fr = ( int(bod[0]+size/2), int(bod[1])+size/2 )
 	to = ( int(bod2[0]+size/2), int(bod2[1])+size/2 )
    
        img.add(img.line(fr, to, stroke=stroke))

    img.save()

def drawPic(name, obj, translist, steps):
    img = svgwrite.Drawing('transformations_' + name + '.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')    
    size = 1000

    for i in range(steps): 
        lines = []
        for bod in obj:
            lines.append(np.dot(translist,[bod[0],bod[1],1]))
              
        #vykresleni jednu transformaciu  
        for idx,bod in enumerate(lines):
            bod2 = lines[(idx+1)%len(lines)]

            fr = ( int(bod[0])+size/2, int(bod[1])+size/2 )
 	    to = ( int(bod2[0])+size/2, int(bod2[1])+size/2 )
    
            img.add(img.line(fr, to, stroke=stroke))

        obj = lines
    img.save()

def getMatrix(a, b, c, d, e, f):
    return np.array([
        [a, b, e], 
        [c, d, f], 
        [0, 0, 1]
    ])


#nedokoncene 
def ferns(filename = "fern", steps = 10):
  translist = []  
#  translist.append(getMatrix(0.849, 0.037, -0.037, 0.849, 75, 183))
#  translist.append(getMatrix(0.197, -0.226, 0.226, 0.197, 400, 49))
#  translist.append(getMatrix(-0.15, 0.283, 0.26, 0.237, 575, 84))
#  translist.append(getMatrix(0, 0, 0, 0.16, 500, 0))

  translist.append(getMatrix(0.5, 0, 0, 0.5, 0, 0))
  translist.append(getMatrix(0.5, 0, 0, 0.5, 0, 500))
  translist.append(getMatrix(0.5, 0, 0, 0.5, 500, 500))

  print translist

  drawPic(filename, square(1000), translist, steps)

#ex()
ferns()



















