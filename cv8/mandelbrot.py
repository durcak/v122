import Image
import colorsys
import math

def getRGB(color):
  rightColor = ()
  for x in color:
    rightColor += (int(round(255*x)),)
  return rightColor
  
def getColorFromNumber(number, numberRange):
  ratio = (float(number)/numberRange)
  
  return getRGB(colorsys.hsv_to_rgb(ratio,1,1))

# Zdroj http://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map
def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum),float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    r = int(max(0, 255*(1 - ratio)))
    b = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b

def julius(size, initial, iterCount, square = ()):
  im = Image.new("RGB", (size, size), (255, 255, 255))
  
  squareSize = square[2]-square[0]
  squareRatio = float(squareSize)/size
  squareRatioY = float(squareSize)/size
  
  for x in range(size):
    for i in range(size):     
      
      xx = ((x*squareRatio+square[0])*4.0/size)-2
      ii = ((i*squareRatio+square[1])*4.0/size)-2
      z1 = complex(xx, ii)
      c = initial
      
      outerIter = 0
      distance = 0
      for j in range(iterCount):
        z1 = z1**2+c
        outerIter += 1
        distance += abs(z1)
        if abs(z1) >2:          
          break
      
      color1 = getColorFromNumber(int(outerIter*255.0/iterCount), 255)
      color2 = getColorFromNumber(int(distance*255/iterCount), 255)
      
      if (abs(z1) < 2):
        im.putpixel((x, i), color2)
      else:
        im.putpixel((x, i), rgb(0,255,abs(z1)*155.0/iterCount))
  
  im.save("julius3.png")
    
def mandelbrot(size, initial, iterCount, square = ()):
  if len(square) < 4:
    square = (0,0,size,size)
    
  im = Image.new("RGB", (size, size), (255, 255, 255))
  z1 = initial
  
  squareSize = square[2]-square[0]
  squareRatio = float(squareSize)/size
  squareRatioY = float(squareSize)/size  
  
  for x in range(size):
    for i in range(size):
      z1 = initial
      xx = ((x*squareRatio+square[0])*3.0/size)-2
      ii = ((i*squareRatio+square[1])*2.0/size)-1
      c = complex(xx, ii)
      
      outerIter = 0
      distance = 0
      for j in range(iterCount):
        z1 = z1**2+c
        outerIter += 1
        distance += abs(z1)
        if abs(z1) >2:          
          break
      
      color1 = getColorFromNumber(outerIter*255.0/iterCount, 255)
      color2 = getColorFromNumber(distance*255/iterCount, 255)
      if (abs(z1) < 2):
         im.putpixel((x, i), rgb(0,255,math.sin(color1*255.0/iterCount)))
      else:
        im.putpixel((x, i), color2)

  
  im.save("mandelbrot6.png")
      
if __name__ == "__main__":  
  #mandelbrot(500, 0, 20, (100, 100, 400, 400) )
  
  julius(500, complex( -0.13, 0.75), 20, (200, 100, 400, 300))
  
