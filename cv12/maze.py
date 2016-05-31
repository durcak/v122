import random
import svgwrite

wall = dict()
visited = dict()
#size = 12	#number of rows or cols

def dfs(x,y,size):

    visited[(x,y)] = 1
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    random.shuffle(directions)

    for i, j in directions:
        cur = (x,y)
        next = (i+x,j+y)

        if next not in wall or abs(x-next[0]) == abs(y-next[1]) : continue     
        if visited[next]: continue

	#natoto niesom hrdy
        if i > 0:
            wall[cur][2] = 0   
            wall[next][0] = 0
        if j > 0:
            wall[cur][1] = 0
            wall[next][3] = 0
        if i < 0:
            wall[cur][0] = 0
            wall[next][2] = 0
        if j < 0:
            wall[cur][3] = 0
            wall[next][1] = 0

        dfs(next[0],next[1],size)

def wallinit(n):
    for i in range(n):
        for j in range(n):
            wall[(i,j)] = [1,1,1,1]
            visited[(i,j)] = 0

def drawmaze(filename,size):
    scale = 50
    svg = svgwrite.Drawing(filename, size=(size*scale,size*scale), profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')

    step = scale
    wlen = scale

    for x in range(size):
        for y in range(size):
            for i, w in enumerate(wall[(x, y)]):
                if not w: continue              
		
                if i == 0: svg.add(svg.line((x*step, y*step), (x*step, y*step + wlen),stroke=stroke))
                if i == 1: svg.add(svg.line((x*step, y*step + wlen), (x*step + wlen, y*step + wlen),stroke=stroke))
                if i == 2: svg.add(svg.line((x*step + wlen, y*step), (x*step + wlen, y*step + wlen),stroke=stroke))
                if i == 3: svg.add(svg.line((x*step, y*step), (x*step + wlen, y*step),stroke=stroke))
                    
    svg.save()

if __name__ == "__main__":
    wallinit(size)
    dfs(0,0,15)

    drawmaze("out.svg",15)

