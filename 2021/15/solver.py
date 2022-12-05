""" Advent of Code solver class """
from pprint import pprint

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[int(x) for x in line] for line in file_handle.read().splitlines()]

def fn(x, y, graph):
    """ Takes x, y and return 00x-00y """
    if x < 0 or y < 0 or x > len(graph[0]) or y > len(graph):
        return -1
    return "{:03d}".format(x)+"-"+"{:03d}".format(y)

def getNode(nodestr, graph):
    """ Takes 00x-00y and returns value of x, y node """
    return graph[int(nodestr[0:3])][int(nodestr[4:7])]

def getTop(nodestr, graph):
    """ Takes 00x-00y and returns neighbour to the top """
    x, y = int(nodestr[0:3]), int(nodestr[4:7])
    if y < 1:
        return ""
    return "{:03d}".format(x)+"-"+"{:03d}".format(y-1)

def getBot(nodestr, graph):
    """ Takes 00x-00y and returns neighbour to the bottom """
    x, y = int(nodestr[0:3]), int(nodestr[4:7])
    if y >= len(graph)-1:
        return ""
    return "{:03d}".format(x)+"-"+"{:03d}".format(y+1)

def getLeft(nodestr, graph):
    """ Takes 00x-00y and returns neighbour to the left """
    x, y = int(nodestr[0:3]), int(nodestr[4:7])
    if x < 1:
        return ""
    return "{:03d}".format(x-1)+"-"+"{:03d}".format(y)

def getRight(nodestr, graph):
    """ Takes 00x-00y and returns neighbour to the right """
    x, y = int(nodestr[0:3]), int(nodestr[4:7])
    if x >= len(graph)-1:
        return ""
    return "{:03d}".format(x+1)+"-"+"{:03d}".format(y)

def dijkstra(g, start):
    shortest = {}
    visited = []
    unvisited = []
    for i, line in enumerate(g):
        for j, _ in enumerate(line):
            unvisited.append(fn(i, j, g))
    
    for node in unvisited:
        shortest[node] = 99999
    
    cur = start
    shortest[start] = 0
    while unvisited:
        neighbours = [getTop(cur, g), getBot(cur, g), getLeft(cur, g), getRight(cur,g )]
        for nb in neighbours:
            if nb != "" and nb not in visited:
                if shortest[nb] > shortest[cur]+getNode(nb, g):
                    shortest[nb] = shortest[cur]+getNode(nb, g)
        visited.append(cur)
        unvisited.remove(cur)
        nextv = 99999
        nextn = "000-000"
        for node in unvisited:
            if shortest[node] < nextv:
                nextv, nextn = shortest[node], node
        cur = nextn
        if cur == fn(int(len(g[0])-1), int(len(g)-1), g):
            break
    return shortest[fn(int(len(g[0])-1), int(len(g)-1), g)]

def task1():
    """ Task 1 solver """
    result = dijkstra(inp, "000-000")
    print("Task 1:", result)

task1()

def task2():
    """ Task 2 solver """
    cave = []
    for i in [1, 2, 3, 4, 5]:
        for k, line in enumerate(inp):
            new = []
            for j in [1, 2, 3, 4, 5]:
                for l, x in enumerate(line):
                    v = x+i+j-2
                    if v > 9:
                        v = (x+i+j-2)%9
                    new.append(v)
            cave.append(new)

    result = dijkstra(cave, "000-000")
    print("Task 2:", result)

task2()
