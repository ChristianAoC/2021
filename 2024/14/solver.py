import time
import re
from math import prod

""" Advent of Code solver class """
startparse = time.time()
sample = False
filename = "input.txt"
maxr = 103
maxc = 101
if sample:
    filename = "sample.txt"
    maxr = 7
    maxc = 11
with open(filename, 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]
p = []
v = []
for line in inp:
    res = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
    p.append((int(res[2]),int(res[1])))
    v.append((int(res[4]),int(res[3])))

endparse = time.time()
print(f"Parsing took {(endparse-startparse)*10**3:.03f}ms")

def task1():
    """ Task 1 solver """
    secs = 100
    newp = []
    q = {"TL":0, "TR":0, "BL":0, "BR":0}
    for i, (r,c) in enumerate(p):
        newp.append(((r+v[i][0]*secs)%maxr, (c+v[i][1]*secs)%maxc))
        if newp[-1][0] < maxr/2-1 and newp[-1][1] < maxc/2-1:
            q["TL"] += 1
        elif newp[-1][0] > maxr/2 and newp[-1][1] < maxc/2-1:
            q["BL"] += 1
        elif newp[-1][0] < maxr/2-1 and newp[-1][1] > maxc/2:
            q["TR"] += 1
        elif newp[-1][0] > maxr/2 and newp[-1][1] > maxc/2:
            q["BR"] += 1
    return prod(q.values())

start = time.time()
print("Task 1 result:", task1(), f" (time: {(time.time()-start)*10**3:.03f}ms)")

def checktree(lines, rows = 3):
    for i in range(rows):
        for col in range(maxc):
            if col < maxc/2-1-i or col > maxc/2+i:
                continue
            else:
                print("yaaaa","i", i, "col-i", col-i, "col+i", col+i, "maxc/2", maxc/2)

# idea: print robots into grid, look for streak
def printgrid(robots, secs):
    g = []
    for i in range(maxr):
        line = []
        for j in range(maxc):
            line.append(".")
        g.append(line)
    for (r, c) in robots:
        if g[r][c] == ".":
            g[r][c] = 1
        else:
            g[r][c] += 1
    # as soon as we find any occurence of more than 15 bots in a row it's probably the "picture"
    # so print that (and see if there's others - spoiler: there isn't)
    for i, line in enumerate(g):
        streak = 0
        l = ""
        for j in line:
            if j == ".":
                if streak > 15:
                    print(secs)
                streak = 0
            else:
                streak += 1

def task2():
    """ Task 2 solver """
    secs = 0
    while secs < maxr*maxc:
        lines = []
        secs += 1
        tree = False
        for i, (r,c) in enumerate(p):
            nr, nc = (r+v[i][0]*secs) % maxr, (c+v[i][1]*secs) % maxc
            lines.append((nr, nc))
        printgrid(lines, secs)

    return ""

start = time.time()
print("Task 2 result:", task2(), f" (time: {(time.time()-start)*10**3:.03f}ms)")
