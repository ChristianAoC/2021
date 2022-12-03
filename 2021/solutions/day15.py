input = [[int(x) for x in line.strip()] for line in open('inputs/15test.txt', 'r')]

### TASK 1
xmax = len(input[0])-1
ymax = len(input)-1
shortestpath = 100000
paths = []



"""
 1  function Dijkstra(Graph, source):
 2
 3      create vertex set Q
 4
 5      for each vertex v in Graph:            
 6          dist[v] ← INFINITY                 
 7          prev[v] ← UNDEFINED                
 8          add v to Q                     
 9      dist[source] ← 0                       
10     
11      while Q is not empty:
12          u ← vertex in Q with min dist[u]   
13                                             
14          remove u from Q
15         
16          for each neighbor v of u still in Q:
17              alt ← dist[u] + length(u, v)
18              if alt < dist[v]:              
19                  dist[v] ← alt
20                  prev[v] ← u
21
22      return dist[], prev[]
"""

"""
def find_lowest_risk(grid):
  n = len(grid)
  risks = np.ones_like(grid)*max_int

  node = (0, 0) # start
  not_visited = {node}
  risks[node] = 0
  while node != (n-1, n-1): # to end
    x, y = node
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      xdx, ydy = x+dx, y+dy
      if not (0 <= xdx < n and 0 <= ydy < n):
        continue
      if risks[xdx, ydy] == max_int:
        not_visited.add((xdx, ydy))
      risks[xdx, ydy] = min(risks[node]+grid[xdx, ydy], risks[xdx, ydy])
    not_visited.remove(node)
    node = reduce(lambda a,b: a if risks[a] < risks[b] else b, not_visited)

  return risks[node]

find_lowest_risk(input)
"""
"""
def recurs(ts, x):
  print(ts)
  ts += str(x)
  if len(ts) == 10:
    return ts
  for i in range(3):
    recurs(ts, i)

recurs("", "0")
"""

"""
def explore(path, x, y):
  path.append((x, y))
  if x==xmax and y==ymax:
    paths.append(path)
    print(path)
    return path
  neighbours = []
  if x<xmax and (x+1,y) not in path: neighbours.append((x+1, y))
  if y<ymax and (x,y+1) not in path: neighbours.append((x, y+1))
  if x>0 and (x-1,y) not in path: neighbours.append((x-1, y))
  if y>0 and (x,y-1) not in path: neighbours.append((x, y-1))
  for neighbour in neighbours:
    explore(path, neighbour[0], neighbour[1])

def explore2(path, x, y, leng, shortest):
  leng += input[x][y]
  if leng<shortest:
    path += str(x)+str(y)+","
    if x==xmax and y==ymax:
      print(leng)
      if leng<shortest:
        shortest = leng
#      paths.append(path)
      return path
    neighbours = []
    if x<xmax and str(x+1)+str(y)+"," not in path: neighbours.append((x+1, y))
    if y<ymax and str(x)+str(y+1)+"," not in path: neighbours.append((x, y+1))
    if x>0 and str(x-1)+str(y)+"," not in path: neighbours.append((x-1, y))
    if y>0 and str(x)+str(y-1)+"," not in path: neighbours.append((x, y-1))
    for neighbour in neighbours:
      explore2(path, neighbour[0], neighbour[1], leng, shortest)
"""
"""
if len(path) > 0:
  print(path)
  print(f"{x},{y},{xmax},{ymax}")
  path.append((x,y))
  if x==xmax and y==ymax:
    print("a")
    paths.append(path)
    return
  neighbours = []
  if x<xmax and (x+1,y) not in path: neighbours.append((x+1, y))
  if y<ymax and (x,y+1) not in path: neighbours.append((x, y+1))
  if x>0 and (x-1,y) not in path: neighbours.append((x-1, y))
  if y>0 and (x,y-1) not in path: neighbours.append((x, y-1))
  for neighbour in neighbours:
    path = explore(path,neighbour[0],neighbour[1])
  return path
"""

"""
visited = []
queue = [(0,0)]
while queue:
  node = queue.pop(0)
  if node not in visited:
    visited.append(node)
    neighbours = []
    x=node[0]
    y=node[1]
    if x<xmax and (x+1,y) not in path: neighbours.append((x+1, y))
    if y<xmax and (x,y+1) not in path: neighbours.append((x, y+1))
    if x>0 and (x-1,y) not in path: neighbours.append((x-1, y))
    if y>0 and (x,y-1) not in path: neighbours.append((x, y-1))
    for neighbour in neighbours:
      queue.append(neighbour)
print(visited)
"""
"""
path.append((x,y))
if x==xmax and y==ymax:
  paths.append(path)
  return
neighbours = []
if x<xmax and (x+1,y) not in path: neighbours.append((x+1, y))
if y<xmax and (x,y+1) not in path: neighbours.append((x, y+1))
if x>0 and (x-1,y) not in path: neighbours.append((x-1, y))
if y>0 and (x,y-1) not in path: neighbours.append((x, y-1))
for neighbour in neighbours:
  path = explore(path,neighbour[0],neighbour[1])
return path
"""
"""
if x<xmax and (x+1,y) not in path:
  path = explore(path,x+1,y)
if y<ymax and (x,y+1) not in path:
  path = explore(path,x,y+1)
if x>0 and (x-1,y) not in path:
  path = explore(path,x-1,y)
if y>0 and (x,y-1) not in path:
  path = explore(path,x,y-1)
return path
"""

#explore([],0,0)
#explore2("",0,0,0,100000)
#print(paths)
