""" Advent of Code solver class """
from pprint import pprint
import numpy as np

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[x for x in line.strip().split()] for line in file_handle]

def task1():
    """ Task 1 solver """
    visited = {(4, 0)}
    head = np.array((4, 0))
    tail = np.array((4, 0))
    for line in inp:
        for _ in range(int(line[1])):
            if line[0] == 'R':
                head[1] += 1
            elif line[0] == 'L':
                head[1] -= 1
            elif line[0] == 'U':
                head[0] -= 1
            elif line[0] == 'D':
                head[0] += 1
            xdiff = head[0]-tail[0]
            ydiff = head[1]-tail[1]
            if abs(xdiff) > 1 or abs(ydiff) > 1:
                if abs(xdiff) > 0 and abs(ydiff) > 0:
                    tail[0] += xdiff/abs(xdiff)
                    tail[1] += ydiff/abs(ydiff)
                elif abs(xdiff) > 1:
                    tail[0] += xdiff/abs(xdiff)
                elif abs(ydiff) > 1:
                    tail[1] += ydiff/abs(ydiff)
            visited.add((tail[0], tail[1]))

    return len(visited)

print("Task 1:", task1())

def move(head, tail):
    xdiff = head[0]-tail[0]
    ydiff = head[1]-tail[1]
    if abs(xdiff) > 1 or abs(ydiff) > 1:
        if abs(xdiff) > 0 and abs(ydiff) > 0:
            tail[0] += xdiff/abs(xdiff)
            tail[1] += ydiff/abs(ydiff)
        elif abs(xdiff) > 1:
            tail[0] += xdiff/abs(xdiff)
        elif abs(ydiff) > 1:
            tail[1] += ydiff/abs(ydiff)
    return tail

def task2():
    """ Task 2 solver """
    rope = []
    for i in range(0, 10):
        rope.append(np.array((15, 11)))
    visited = {(15, 11)}
    for line in inp:
        for _ in range(int(line[1])):
            if line[0] == 'R':
                rope[0][1] += 1
            elif line[0] == 'L':
                rope[0][1] -= 1
            elif line[0] == 'U':
                rope[0][0] -= 1
            elif line[0] == 'D':
                rope[0][0] += 1
            for i in range(1, 10):
                rope[i] = move(rope[i-1], rope[i])
                visited.add((rope[9][0], rope[9][1]))
        """
        vis = np.full((21, 26), '.')
        for i, elem in enumerate(rope):
            if i == 0:
                i = 'H'
                vis[rope[0][0]][rope[0][1]] = 'H'
            else:
                vis[rope[i][0]][rope[i][1]] = i
        for line in vis:
            output = ""
            for x in line:
                output += x
            print(output)
        """
    return len(visited)

print("Task 2:", task2())
