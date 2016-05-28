import collections
import numpy
from numpy         import array

start       = [0,0]
maze        = numpy.loadtxt('maze1.txt',delimiter=" ")
size        = len(maze)
paths       = []
stack       = []

def findPath(pos):
	# DFS algorithm
    	stack.append(pos)

	# check if you are in finish
	if maze[pos[0]][pos[1]] == 0:
	    paths.append( stack[::] )
	    stack.pop()
	    #print "Possible path"
	    #print STACK
	    return
	else:
	    for d in [[0,1],[1,0],[-1,0],[0,-1]]:
		# next position
		new_pos = list( pos + maze[pos[0]][pos[1]] * array( d ))

		if new_pos in stack:  #its cyrcle
		    continue
		#check if pos is in maze
                if not ((0 <= new_pos[0] < size and (0 <= new_pos[1] < size))):
                    continue
                print new_pos
		findPath( new_pos )
	    else:
		stack.pop()
 	return

#read maze with number length on first line
def loadData(fpath):

    with open(fpath) as f:
        n = int(f.readline())
        data = [[None]*n for i in range(n)]

        for i in range(n):
            line = f.readline().rstrip().split()
            #print line
            for j in range(n):
                #print int(line[j])
                data[i][j]=(int(line[j]))
        return data

if __name__ == "__main__":
    findPath([0,0])
    print 'Number of solutions:', len(paths)
    for i in range(len(paths)):
	print 'Solution',i+1,':', paths[i]
"""
Number of solutions: 2
Solution 1 : [[0, 0], [0.0, 2.0], [2.0, 2.0], [3.0, 2.0], [3.0, 3.0]]
Solution 2 : [[0, 0], [0.0, 2.0], [2.0, 2.0], [3.0, 2.0], [3.0, 1.0], [3.0, 0.0], [3.0, 3.0]]

"""

