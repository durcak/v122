import Image
import colorsys
import math

import sys,os,time
from threading import Thread,Event

#pouzitim vlakien sa rychlost programu zlepsila takmer 4krat
class ct1(Thread):
    def __init__(self,img,size,square,squareSize,squareRatio,iterCount,x):
        Thread.__init__(self)

        self.iterCount = iterCount
        self.x = x
        self.size = squareSize
        self.squareRatio = squareRatio
	self.square = square
        self.im = img
	self.size = size

    def run(self):
      for i in range(self.size):
      	xx = ((self.x*self.squareRatio+self.square[0])*4.0/self.size)-2
      	ii = ((i*self.squareRatio+self.square[1])*4.0/self.size)-2
        #xx = (self.x**4.0/self.size)-2
      	#ii = (i*4.0/self.size)-2
      	z1 = complex(xx, ii)
      
      	for j in range(self.iterCount):
            if abs(z1) < 0.000001:
               continue
            z1 = z1-(z1**3-1)/(3*z1**2)
        temp = 255
        red = int(temp - temp/2*abs(z1-1))
        green = int(temp - temp/2*abs(z1-complex(-0.5, math.sqrt(3)/2)))
        blue = int(temp - temp/2*abs(z1- complex(-0.5, -math.sqrt(3)/2)))
      
     
        shade = (red, green, blue)
      
        self.im.putpixel((self.x,i), shade)


def newton(size, iterCount, square):
  img = Image.new("RGB", (size, size), (255, 255, 255))
   
  squareSize = square[2]-square[0]
  squareRatio = float(squareSize)/size 
 
  for x in range(0,size,4):
      #potrebne doriesit size mod 4 == 0 alebo podmienky pred starom vlakien
      t1 = ct1(img,size,square,squareSize,squareRatio,iterCount,x)
      t2 = ct1(img,size,square,squareSize,squareRatio,iterCount,x+1)
      t3 = ct1(img,size,square,squareSize,squareRatio,iterCount,x+2)
      t4 = ct1(img,size,square,squareSize,squareRatio,iterCount,x+3)
      t1.start()
      t2.start()
      t3.start()
      t4.start() 
 
  img.save("newtonfractal.png")
      
if __name__ == "__main__":
  
  newton(800, 20, (0, 0, 800, 800))
