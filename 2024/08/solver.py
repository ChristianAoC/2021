import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

""" Advent of Code solver class """
with open('sample.txt', 'r', encoding='utf8') as file_handle:
    inp = [[x for x in line.strip()] for line in file_handle.readlines()]

maxr = len(inp)
maxc = len(inp[0])

"""
# animation - finish later
map = {}
plot = []
for row, line in enumerate(inp):
    newline = []
    for col, val in enumerate(line):
        if val == ".":
            newline.append(0)
            continue
        elif val not in map:
            map[val] = random.random()
        newline.append(map[val])
    plot.append(newline)

fig = plt.figure()
im = plt.imshow(plot, animated=True)
plt.show()

def updatefig(*args):
    im.set_array(plot)
    return im
ani = animation.FuncAnimation(fig, updatefig, blit=True)
plt.show()
"""

antennas = {}
for row, line in enumerate(inp):
    for col, value in enumerate(line):
        if value == ".":
            continue
        if value in antennas:
            antennas[value].add((row,col))
        else:
            antennas[value] = set()
            antennas[value].add((row,col))

def task1():
    """ Task 1 solver """
    antinodes = set()
    for ant in antennas:
        for a in antennas[ant]:
            for b in antennas[ant]:
                if a != b:
                    an1 = (a[0]+(a[0]-b[0]), a[1]+(a[1]-b[1]))
                    an2 = (b[0]+(b[0]-a[0]), b[1]+(b[1]-a[1]))
                    if 0 <= an1[0] < maxr and 0 <= an1[1] < maxc:
                        antinodes.add(an1)
                    if 0 <= an2[0] < maxr and 0 <= an2[1] < maxc:
                        antinodes.add(an2)
    return len(antinodes)

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    antinodes = set()
    for ant in antennas:
        for a in antennas[ant]:
            for b in antennas[ant]:
                if a != b:
                    i = 0
                    diffr = a[0]-b[0]
                    diffc = a[1]-b[1]
                    while 0 <= a[0]+diffr*i < maxr and 0 <= a[1]+diffc*i < maxc:
                        antinodes.add((a[0]+diffr*i, a[1]+diffc*i))
                        i += 1

                    i = 0
                    diffr = b[0]-a[0]
                    diffc = b[1]-a[1]
                    while 0 <= b[0]+diffr*i < maxr and 0 <= b[1]+diffc*i < maxc:
                        antinodes.add((b[0]+diffr*i, b[1]+diffc*i))
                        i += 1
    for row, line in enumerate(inp):
        for col, el in enumerate(line):
            if (row, col) in antinodes:
                inp[row][col] = "#"
    return len(antinodes)

print("Task 2:", task2())
