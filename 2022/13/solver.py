""" Advent of Code solver class """
from pprint import pprint
from copy import deepcopy

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[pair.strip() for pair in line.split('\n')] for line in file_handle.read().split('\n\n')]

i_pairs = []
for pair in inp:
    i_pairs.append([eval(pair[0]),eval(pair[1])])

def compare(left, right):
    res = None
    while len(left) > 0 and len(right) > 0:
        l = left.pop(0)
        r = right.pop(0)
        if isinstance(l, int) and isinstance(r, int):
            if l != r:
                return l < r
        elif isinstance(l, list) and isinstance(r, list):
            res = compare(l, r)
            if res != None:
                return res
        elif isinstance(l, list) and isinstance(r, int):
            res = compare(l, [r])
            if res != None:
                return res
        elif isinstance(l, int) and isinstance(r, list):
            res = compare([l], r)
            if res != None:
                return res
    if len(left) > len(right):
        res = False
    elif len(left) < len(right):
        res = True
    return res

def task1():
    """ Task 1 solver """
    i_result = 0
    for i, pair in enumerate(i_pairs):
        if compare(pair[0], pair[1]):
            i_result += i+1
    return i_result

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    with open('input.txt', 'r', encoding='utf8') as file_handle:
        two = file_handle.read().replace('\n\n', '\n').splitlines()
    first = 1
    second = len(two)+2
    for line in two:
        if compare(eval(line), [[2]]):
            first += 1
        if compare([[6]], eval(line)):
            second -= 1
    print(first, second)
    return first * second

print("Task 2:", task2())
