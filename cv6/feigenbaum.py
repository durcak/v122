import Image

def feigenbaum(filename, size, itern, Xa, Xb, Ya, Yb):
   img = Image.new("RGB", (size, size), (255, 255, 255))
  
   zoomY = (Yb-Ya)
  
   for i in xrange(size):    
     r = Xa + i*(Xb-Xa)/float(size-1) 
     xt = i/float(itern)    
     xt = 0.5
     for j in xrange(itern):
      
       xt = r*xt*(1-xt)
     
       if j > itern/2:        
         if xt >= Ya and xt <= Yb:
	   x = int(1.0*i*size/itern)
	   y = int((xt-Ya)*size/zoomY)
           img.putpixel((i,y), (15, 58, 178))
      
  
   img.show()
   img.save(filename)


if __name__ == "__main__":
   feigenbaum("feigenbaum.png", 600, 1500, 3.5, 4., 0.2, 0.5)
   feigenbaum("feigenbaum2.png", 600, 1500, 2.5, 4., 0.0, 1.0)

