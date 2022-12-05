""" Advent of Code solver class """
from copy import deepcopy

with open('sample.txt', 'r', encoding='utf8') as file_handle:
    inp1, inp2 = [x.split('\n') for x in file_handle.read().split('\n\n')]

stack = []
for s in inp1.pop().split():
    stack.append([])

for line in reversed(inp1):
    for i, x in enumerate(line):
        if x not in [' ', '[', ']']:
            stack[(i-1)//4].append(x)

instructions = []
for line in inp2:
    instructions.append([int(x) for x in line.split() if x not in ['to', 'from', 'move']])

def task1():
    """ Task 1 solver """
    result = ""
    stack_copy = deepcopy(stack)
    for instr in instructions:
        i = 0
        while i < instr[0]:
            stack_copy[instr[2]-1].append(stack_copy[instr[1]-1].pop())
            i += 1
    for s in stack_copy:
        if s != []:
            result += s[-1]
    print(result)

task1()

def task2():
    """ Task 2 solver """
    result = ""
    for instr in instructions:
        i = 0
        popped = []
        while i < instr[0]:
            popped.append(stack[instr[1]-1].pop())
            i += 1
        stack[instr[2]-1] = stack[instr[2]-1] + popped[::-1]
    for s in stack:
        if s != []:
            result += s[-1]
    print(result)

task2()
