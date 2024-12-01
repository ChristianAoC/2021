import numpy as np

""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = np.rot90(np.array([line.split() for line in file_handle])).astype(int)
    inp[0].sort()
    inp[1].sort()
    print(inp)

def task1():
    """ Task 1 solver """
    result = []
    for i in range(len(inp[0])):
        result.append(abs(inp[0][i]-inp[1][i]))
    return np.sum(result)

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    result = 0
    count = {}
    for i in inp[1]:
        if i not in count.keys():
            count[i] = 0
        count[i] += 1
    for i in range(len(inp[0])):
        if inp[0][i] in count.keys():
            result += inp[0][i] * count[inp[0][i]]
    return result

print("Task 2:", task2())
