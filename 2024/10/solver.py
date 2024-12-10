import itertools

""" Advent of Code solver class """

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[int(x) for x in line.strip()] for line in file_handle]
#print(inp)

maxr = len(inp)
maxc = len(inp[0])
trailheads = set()
for r, line in enumerate(inp):
    for c, v in enumerate(line):
        if v == 0:
            trailheads.add((r, c))

def traverse(nines, r, c):
    for dir in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        #print("r+dir[0]",r+dir[0],"c+dir[1]",c+dir[1],"diff",inp[r+dir[0]][c+dir[1]] - inp[r][c])
        if 0 <= r+dir[0] < maxr and 0 <= c+dir[1] < maxc:
            if (inp[r+dir[0]][c+dir[1]] - inp[r][c]) == 1:
                if inp[r+dir[0]][c+dir[1]] == 9:
                    nines.add((r+dir[0],c+dir[1]))
                else:
                    traverse(nines, r+dir[0], c+dir[1])
    return nines

def task1():
    """ Task 1 solver """
    result = 0
    for t in trailheads:
        nines = set()
        result += len(traverse(nines, t[0], t[1]))
    return result

print("Task 1:", task1())

def mapTrails(trails, r, c):
    for dir in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        #print("r+dir[0]",r+dir[0],"c+dir[1]",c+dir[1],"diff",inp[r+dir[0]][c+dir[1]] - inp[r][c])
        if 0 <= r+dir[0] < maxr and 0 <= c+dir[1] < maxc:
            if (inp[r+dir[0]][c+dir[1]] - inp[r][c]) == 1:
                trails[inp[r+dir[0]][c+dir[1]]].add(( r+dir[0], c+dir[1] ))
                if inp[r+dir[0]][c+dir[1]] < 9:
                    mapTrails(trails, r+dir[0], c+dir[1])
    return trails

def task2():
    """ Task 2 solver """
    result = 0
    for t in trailheads:
        trails = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
            9: set()
        }
        trails[0].add(t)
        trails = mapTrails(trails, t[0], t[1])
        all = set(itertools.product(trails[0],trails[1],trails[2],trails[3],trails[4],trails[5],trails[6],trails[7],trails[8],trails[9]))
        correct = 0
        for trail in all:
            for num, coords in enumerate(trail):
                if num == 0:
                    continue
                if trail[num-1] not in [
                    (coords[0]-1, coords[1]),
                    (coords[0]+1, coords[1]),
                    (coords[0], coords[1]-1),
                    (coords[0], coords[1]+1)
                    ]:
                    break
                elif num == 9:
                    correct += 1
        result += correct
    return result

print("Task 2:", task2())
