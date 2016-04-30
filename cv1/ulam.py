from PIL import Image
import numpy
import math

side_len = 400

def is_prime2(x):
    if x == 1 or (x % 2 == 0 and x > 2):
        return False
    elif x == 2:
        return True  
    for n in range(2, int(math.sqrt(x))):
        if x % n ==0:
            return False
    return True

def count_spiral(is_on_spiral, image_name):
    img = Image.new('RGB', (side_len + 1, side_len + 1), 'white')
    pixels = img.load()

    x, y = 0, 0 #suradnice

    	   # right    up     left    down
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    actual_direction = 0 # 0       1      2       3

    steps = 1 # number of steps done in a direction

    i = 0
    while i < side_len**2:
        for j in range(0,2):
            for k in range(0, steps):
                i += 1

                if is_on_spiral(i):
                    pixels[side_len//2+x,side_len//2+y] = (0,0,0) # setting black pixel 

                pom = moves[actual_direction]
                x += pom[0]
                y += pom[1]

            actual_direction = (actual_direction + 1) % 4

        steps += 1

    img.save(image_name)

count_spiral(is_prime2, 'ulam_prime.bmp')
count_spiral(lambda x: x % 5 == 0, 'ulam_5.bmp')
count_spiral(lambda x: x % 8 == 0, 'ulam_8.bmp')

