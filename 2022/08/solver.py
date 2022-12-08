""" Advent of Code solver class """
from pprint import pprint
import numpy as np

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]

def task1():
    """ Task 1 solver """
    visible = {(0, 0)}
    largest_top = [-1 for x in inp[0]]
    for j, row in enumerate(inp):
        # check from left
        largest = -1
        i = 0
        while largest < 9 and i < len(row):
            if int(row[i:i+1]) > largest:
                largest = int(row[i:i+1])
                visible.add((i, j))
            i += 1

        # check from right
        largest = -1
        i = len(row)
        while largest < 9 and i > 0 and (i-1, j) not in visible:
            if int(row[i-1:i]) > largest:
                largest = int(row[i-1:i])
                visible.add((i-1, j))
            i -= 1
        # check from top
        for i, _ in enumerate(row):
            if int(row[i:i+1]) > largest_top[i]:
                largest_top[i] = int(row[i:i+1])
                visible.add((i, j))
    # check from bottom
    largest_bot = [-1 for x in inp[0]]
    for j, row in enumerate(reversed(inp)):
        for i, height in enumerate(row):
            if int(height) > largest_bot[i]:
                largest_bot[i] = int(height)
                visible.add((i, len(inp)-j-1))
    return len(visible)

print("Task 1:", task1())

def check(row, pointer):
    """ Check to the right of pointer for view """
    view = 1
    if pointer == len(row)-1:
        view = 0
    while pointer+view < len(row)-1 and row[pointer+view] < row[pointer]:
        view += 1
    return view

def task2():
    """ Task 2 solver """
    result = 0
    inp2 = [[x for x in line] for line in inp]
    aoc = np.array(inp2)
    aoct = aoc.transpose()
    for i, row in enumerate(aoc):
        for j, _ in enumerate(row):
            view = check(row, j) * check(row[::-1], len(row)-1-j) * check(aoct[j], i) * check(aoct[j][::-1], len(row)-1-i)
            if view > result:
                result = view
    return result

print("Task 2:", task2())
