import matplotlib.pyplot as plt
from math import sqrt
from random import choice


def loadData(fpath):
    data = []
    for line in open(fpath):
        x,y = line.rstrip().split()
        x,y = float(x), float(y)
        data.append((x,y))

    return data

def dist(A, B):
    return sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 )

def kMeans(points, k, iterations=20):
    distance      = lambda (a,b),(c,d): ( (a-c)**2 + (b-d)**2 ) ** 0.5
    getsecond     = lambda (a,b): b
    centers       = [ choice(points) for _ in range(k) ]
     
    for i in xrange(iterations):
        totals = [(0,0)] * k
        counts = [ 0.0 ] * k
 
        for pt in points:
            excentricities = [ distance(pt, ctr) for ctr in centers ]
            index          = min( enumerate(excentricities), key=getsecond )[0]
            tx, ty         = totals[index]
            totals[index]  = tx + pt[0], ty + pt[1]
            counts[index] += 1
 
        centers = [ n and (x/n, y/n) or (0,0) for (x,y),n in zip(totals, counts) ]
 
    return centers

#vyskresli vsetky body jednou farbou, centra modrou
def drawplot(centers, points, name):
    y = [y for (x,y) in centers]
    x = [a for (a,b) in centers]
    
    plt.plot(*zip(*points), marker='o', color='r', ls='')
    plt.scatter(x,y)
    plt.show()
    #plt.savefig(name + '.png')

#vykresli body podla skupiny do ktorej patria
def drawplot2(centers, points, name):
    plt.figure()
    colors = list('rgkcmyb')   #moze nastat problem ak by bolo k moc velke,budu chybat farby

    #print centers
    y = [y for (x,y) in centers]
    x = [a for (a,b) in centers]   
    plt.scatter(x,y)

    getsecond     = lambda (a,b): b
    groups = [[] for _ in range(len(centers))]

    for pt in points:
        excentricities = [ dist(pt, ctr) for ctr in centers ]
        index          = min( enumerate(excentricities), key=getsecond )[0]
        groups[index].append(pt)

    for i in range(len(centers)):
        plt.plot(*zip(*groups[i]), marker='o', color=colors[i], ls='')
    
	
    plt.show()
    plt.savefig(name + '.png')

    return groups

### Main
if __name__ == "__main__":
    points = loadData('faithful.txt')
    centers = kMeans(points, 2)
    drawplot2(centers,points,'kmeans-plot')




