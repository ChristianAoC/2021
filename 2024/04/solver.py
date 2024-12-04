import re
""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[x for x in line.strip()] for line in file_handle]

max = len(inp)
word = "XMAS"

def checkWord(row, col, x, y, i):
    if 0 <= (row+y) < max and 0 <= (col+x) < max:
        if inp[row+y][col+x] == word[i]:
            if i == 3:
                return 1
            else:
                return checkWord(row+y, col+x, x, y, i+1)
    return 0

def task1():
    """ Task 1 solver """
    result = 0
    for row in range(max):
        for col in range(max):
            if inp[row][col] == "X":
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if x != 0 or y != 0:
                            result += checkWord(row, col, x, y, 1)
    return result

print("Task 1:", task1())

def checkCross(row, col):
    if 0 < row < max-1 and 0 < col < max-1:
        if sorted([inp[row-1][col-1],inp[row+1][col+1]]) == ['M', 'S'] and sorted([inp[row-1][col+1],inp[row+1][col-1]]) == ['M', 'S']:
            return 1
    return 0

def task2():
    """ Task 2 solver """
    result = 0
    for row in range(max):
        for col in range(max):
            if inp[row][col] == "A":
                result += checkCross(row, col)
    return result

print("Task 2:", task2())
