""" Advent of Code solver class """
from pprint import pprint
from copy import deepcopy

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[ord(x) for x in line.strip()] for line in file_handle]

start = [0, 0]
end = [0, 0]
for i, line in enumerate(inp):
    for j, x in enumerate(line):
        if x == ord('S'):
            inp[i][j] = ord('a')
            start = [i, j]
        if x == ord('E'):
            inp[i][j] = ord('z')
            end = [i, j]

def dijkstra(g, start, two=False):
    """ Using Dijkstra here, but all weights set to 1 and neighbour constraints """
    shortest = []
    visited = []
    unvisited = []
    for i, line in enumerate(g):
        row = []
        for j, _ in enumerate(line):
            unvisited.append([i, j])
            if two == True and g[i][j] == ord('a'):
                row.append(0)
            else:
                row.append(99999)
        shortest.append(row)

    cur = start
    shortest[cur[0]][cur[1]] = 0

    while unvisited:
        neighbours = [[cur[0]-1, cur[1]], [cur[0]+1, cur[1]], [cur[0], cur[1]-1], [cur[0], cur[1]+1]]
        for nb in neighbours:
            if nb in unvisited and nb not in visited and g[nb[0]][nb[1]]-g[cur[0]][cur[1]] < 2:
                if shortest[nb[0]][nb[1]] > shortest[cur[0]][cur[1]]+1:
                    shortest[nb[0]][nb[1]] = shortest[cur[0]][cur[1]]+1
        visited.append(cur)
        unvisited.remove(cur)
        nextv = 99999
        nextn = start
        for node in unvisited:
            if shortest[node[0]][node[1]] <= nextv:
                nextv, nextn = shortest[node[0]][node[1]], node
        cur = nextn
    return shortest[end[0]][end[1]]

def task1():
    """ Task 1 solver """
    one = deepcopy(inp)
    result = dijkstra(one, start)
    return result

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    two = deepcopy(inp)
    result = dijkstra(two, start, True)
    return result

print("Task 2:", task2())
