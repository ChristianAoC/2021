""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[x for x in line.strip()] for line in file_handle]

lab1 = inp.copy()
maxr = len(inp)-1
maxc = len(inp[0])-1
start = []
for row, val in enumerate(lab1):
    for col, val in enumerate(lab1[row]):
        if lab1[row][col] == "^":
            start = [row, col]
visited = set()

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

def move(grid, row, col, p1 = False, obstacle = (-1, -1)):
    seen = set()
    curdir = 0

    while 0 < row < maxr and 0 < col < maxc:
        if grid[row][col] != "#" and p1:
            visited.add((row, col))

        dr = directions[curdir][0]
        dc = directions[curdir][1]
        if grid[row+dr][col+dc] == "#" or obstacle == (row+dr, col+dc):
            if (row, col, directions[curdir]) in seen:
                return 1
            seen.add((row, col, directions[curdir]))
            curdir = (curdir + 1) % 4
        elif dr != 0:
            row += dr
        else:
            col += dc
    return 0

def task1():
    """ Task 1 solver """
    move(lab1, start[0], start[1], True)
    return len(visited) + 1

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    result = 0
    for coord in visited:
        result += move(lab1, start[0], start[1], False, coord)
    
    return result + 1

print("Task 2:", task2())
