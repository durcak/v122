import numpy as np
from PIL import Image
from math import sqrt, sin


def gcd_mod(u, v):
    steps = 0
    while v:
        u, v = v, u % v
        steps += 1
    return steps

def gcd_sub(u, v):
    steps = 0
    while u != v:
        steps += 1
        if u > v:
            u = u - v
        else:
            v = v - u
    return steps

# Zdroj http://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map
def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum),float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    r = int(max(0, 255*(1 - ratio)))
    b = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b

img = Image.new('RGB', (400,400), 'black')
pixels = img.load()

steps = np.zeros(shape=(img.size[0], img.size[1]))
for i in range(img.size[0]):
    for j in range(img.size[1]):
        steps[i,j] = gcd_mod(i + 1, img.size[1] - j)

m = np.amax(steps)
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = rgb(0, m, steps[i,j])

img.save('gcd_steps.png')
