#!/usr/bin/env python

import svgwrite
import colorsys

def pascals_triangle(n):

    # n must by > 0

    layers = [[1]]
    for i in xrange(n - 1):
        layers.append([1])
        for j in xrange(i):
            layers[-1].append(layers[-2][j] + layers[-2][j+1])
        layers[-1].append(1)
        
    return layers


def different_colors(N):       
# code from http://stackoverflow.com/questions/876853/generating-color-ranges-in-python

    HSV_tuples = [(x * 1.0 /  N, 1, 0.85) for x in range(N) ]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb( *x ), HSV_tuples)

    RGB_tuples = map(lambda x: tuple(map(lambda y: int(y * 255),x)),RGB_tuples)

    return RGB_tuples 


def plot_pascals_triangle(n, mod=3, side=10, filename=''):

    # initialize drawing canvas, create layers and colors
    img = svgwrite.drawing.Drawing() 
    colors = different_colors(mod) 
    layers = pascals_triangle(n) 
    

    for y in range(n):
        for x in range( len( layers[ y ] ) ):
            # off set
            nx = n/2*side - y * side / 2 + x * side - side / 2
            color = colors[ (layers[y][x] + 2) % mod ]
            img.add( img.rect(insert = (nx, y * side) , size   = (side, side), \
			    				fill   = 'rgb' + str(color),\
                            				stroke = 'black'))

    img.saveas( 'img/'+ filename + '.svg')
    
    return


if __name__ == '__main__':
    plot_pascals_triangle(30, mod=5, filename='pascals_triangle')
