""" Advent of Code solver class """
from pprint import pprint
from copy import deepcopy

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[[int(x) for x in coords.split(',')] for coords in line.split(' -> ')] for line in file_handle.read().splitlines()]

air = '.'
orig_start = [500, 0]
orig_min = [99999, 99999]
orig_max = [0, 0]
for line in inp:
    for coord in line:
        if coord[0] < orig_min[0]:
            orig_min[0] = coord[0]
        if coord[1] < orig_min[1]:
            orig_min[1] = coord[1]
        if coord[0] > orig_max[0]:
            orig_max[0] = coord[0]
        if coord[1] > orig_max[1]:
            orig_max[1] = coord[1]

if orig_start[0] < orig_min[0]:
    orig_min[0] = orig_start[0]
if orig_start[1] < orig_min[1]:
    orig_min[1] = orig_start[1]
if orig_start[0] > orig_max[0]:
    orig_max[0] = orig_start[0]
if orig_start[1] > orig_max[1]:
    orig_max[1] = orig_start[1]

def flow(cave, row, col):
    """ Let the sane flow! One at a time """
    placed = False
    for i in range(row, len(cave)):
        if cave[i][col] != air:
            if cave[i][col-1] == air:
                placed = flow(cave, i, col-1)
            elif cave[i][col+1] == air:
                placed = flow(cave, i, col+1)
            elif cave[i-1][col] == air:
                cave[i-1][col] = 'o'
                placed = True
            break
    return placed

def task1():
    """ Task 1 solver """
    # rock = #, air = ., sand_source = +, sand_rest = o
    shift = orig_min[0]
    start = [orig_start[0]-shift, orig_start[1]]
    max = [orig_max[0]-shift, orig_max[1]]

    cave = []
    for i in range(max[1]+1):
        row = []
        for j in range(max[0]+1):
            if i == start[1] and j == start[0]:
                row.append('+')
            else:
                row.append(air)
        cave.append(row)

    one = []
    for line in inp:
        newline = []
        last = [-1, -1]
        for coord in line:
            newline.append([coord[0]-shift, coord[1]])
            if last[0] > -1:
                if newline[-1][0] > last[0]:
                    for i in range(last[0], newline[-1][0]+1):
                        cave[last[1]][i] = '#'
                elif newline[-1][0] < last[0]:
                    for i in range(newline[-1][0], last[0]+1):
                        cave[last[1]][i] = '#'
                if newline[-1][1] > last[1]:
                    for i in range(last[1], newline[-1][1]+1):
                        cave[i][last[0]] = '#'
                elif newline[-1][1] < last[1]:
                    for i in range(newline[-1][1], last[1]+1):
                        cave[i][last[0]] = '#'
            last = newline[-1]
        one.append(newline)

    result = 0
    while flow(cave, start[1]+1, start[0]):
        result += 1
        #pprint([''.join(line) for line in cave])
    return result

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    extend = 100
    shift = orig_min[0]-extend
    start = [orig_start[0]-shift, orig_start[1]]
    max = [orig_max[0]-shift+extend, orig_max[1]+2]

    cave = []
    for i in range(max[1]+1):
        row = []
        for j in range(max[0]+1):
            if i == start[1] and j == start[0]:
                row.append('+')
            elif i == max[1]:
                row.append('#')
            else:
                row.append(air)
        cave.append(row)

    one = []
    for line in inp:
        newline = []
        last = [-1, -1]
        for coord in line:
            newline.append([coord[0]-shift, coord[1]])
            if last[0] > -1:
                if newline[-1][0] > last[0]:
                    for i in range(last[0], newline[-1][0]+1):
                        cave[last[1]][i] = '#'
                elif newline[-1][0] < last[0]:
                    for i in range(newline[-1][0], last[0]+1):
                        cave[last[1]][i] = '#'
                if newline[-1][1] > last[1]:
                    for i in range(last[1], newline[-1][1]+1):
                        cave[i][last[0]] = '#'
                elif newline[-1][1] < last[1]:
                    for i in range(newline[-1][1], last[1]+1):
                        cave[i][last[0]] = '#'
            last = newline[-1]
        one.append(newline)

    result = 0
    while flow(cave, start[1]+1, start[0]):
        result += 1
    return result+1

print("Task 2:", task2())
