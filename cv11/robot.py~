import collections
import numpy
from numpy  import array
import sys

start       = [0,0]
maze        = numpy.loadtxt('robot.txt',delimiter=" ",dtype='str')
size        = len(maze)
paths       = []
stack       = []
distances   = []

def findPath(pos, r, penal):
	# DFS algorithm
    	stack.append(pos)

	# check if you are in finish
	if maze[pos[0]][pos[1]] == 'F':
	    paths.append( stack[::] )
            distances.append(penal)
	    stack.pop()

	    return
	else:
	    for d in [[0,1],[1,0],[-1,0],[0,-1]]:
		# next position
		new_pos = list( pos + array( d ))
                #print new_pos

		#check if pos is in maze
                if not ((0 <= new_pos[0] < size and (0 <= new_pos[1] < size))):
                    continue
		if new_pos in stack or maze[new_pos[0]][new_pos[1]] == 'W':  #its cyrcle or wall
		    continue
                if r == d:     #no rotation, 
		   penal += 1  #lower penalization
		else:
		   penal += 2  #higher penalization
		findPath( new_pos, d, penal)
	    else:
		stack.pop()
		penal = 0
 	return

def printAllSolutions():
    print 'Number of solutions:', len(paths)

    for i in range(len(paths)):
	print 'Solution',i+1,':', paths[i]

    print 'Best solution :', paths[distances.index(min(distances))]

def drawMaze(sol = True):   #False print maze without solution
    best = distances.index(min(distances))
    for i in range(size):
        for j in range(size):
	    if [i,j] in paths[best] and sol:
               sys.stdout.write(' .')
            else:
               sys.stdout.write(' ' + maze[i][j])
        print

if __name__ == "__main__":
    findPath([0,0],[0,1],0)

    drawMaze(False)
    drawMaze()

#Maze
"""
 S o o o o o o
 o o W W W W o
 W o o W W W o
 W W o o W W o
 W W W o o W o
 W W W W o o o
 W W W W W W F
"""
#Solution
"""
 . . . . . . .
 o o W W W W .
 W o o W W W .
 W W o o W W .
 W W W o o W .
 W W W W o o .
 W W W W W W .

"""

   
