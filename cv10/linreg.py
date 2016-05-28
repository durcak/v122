import matplotlib.pyplot as plt
from math import sqrt
import numpy as np


def loadData(fpath):
    data = []
    for line in open(fpath):
        x,y = line.rstrip().split()
        x,y = float(x), float(y)
        data.append((x,y))

    return data

#grid search 
def regression(points):
    sum_x = 0
    sum_y = 0
    sum_xx = 0
    sum_xy = 0

    for x,y in points:
        sum_xy += x*y
        sum_xx += x*x
        sum_x  += x
      	sum_y  += y

    n = float(len(points))
               
    a  = n * sum_xy - sum_x * sum_y
    a /= n * sum_xx - sum_x * sum_x
    b  = (sum_y - a * sum_x) / n
 
    return a, b

def drawplot(points, name, a, b, org = (0, 0)):

    fig  = plt.figure(figsize=(23.5, 23.5))
    x, y = zip(*points)
    plt.plot(x, y, 'ro', markersize=8.)
    min_x = min(x)
    max_x = max(x)  
    plt.plot((min_x, max_x), (min_x*a+b, max_x*a+b))
    
    #vykreslime original krivku, z ktorej boli generovane body
    if org != (0,0):
        a, b = org
    	plt.plot((min_x, max_x), (min_x*a+b, max_x*a+b), color= 'k')   

    plt.show()
    fig.savefig(name + '.png')

def dataGenerate(a, b, n, ln=False):

    x = np.arange(0, n)
    print x
    if ln:
        y = a * x + b + np.random.lognormal(0, 4, n)
    else:
        y = a * x + b + np.random.normal(0, 100, n)
    return zip(x, y)


if __name__ == "__main__":
    #points = loadData('linreg.txt')
    #a,b = regression(points)
    #drawplot(points,'linreg',a,b)

    points2 = dataGenerate(10,2,50,True)
    a, b = regression(points2)
    drawplot(points2,'linreg3',a,b,(10,2))



