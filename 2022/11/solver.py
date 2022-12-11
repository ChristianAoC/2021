""" Advent of Code solver class """
from pprint import pprint
from copy import deepcopy

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = file_handle.read().split("\n\n")

inp_m = []
for m in inp:
    op = {"Items": [], "Op": "", "Opval": 0, "Test": 0, "True": 0, "False": 0}
    for line in m.split("\n"):
        if line.startswith("  Start"):
            op["Items"] = [int(x.strip()) for x in line.split(':')[1].split(',')]
        elif line.startswith("  Op"):
            op["Op"] = line[23:24]
            op["Opval"] = line.split(op["Op"])[1].strip()
        if line.startswith("  Test"):
            op["Test"] = int(line.split(' ')[-1])
        if line.startswith("    If true"):
            op["True"] = int(line.split(' ')[-1])
        if line.startswith("    If false"):
            op["False"] = int(line.split(' ')[-1])
    inp_m.append(op)

def throws(monkeys, inspects, part):
    """ Monkey throw action 1 """
    for i, m in enumerate(monkeys):
        copy = deepcopy(m["Items"])
        for item in copy:
            worry = item
            if m["Opval"] == "old":
                opval = worry
            else:
                opval = int(m["Opval"])
            if m["Op"] == "+":
                worry += opval
            elif m["Op"] == "*":
                worry *= opval
            if part == 1:
                worry //= 3
            else:
                worry %= m["Supermod"]
            if worry % m["Test"] == 0:
                monkeys[m["True"]]["Items"].append(worry)
            else:
                monkeys[m["False"]]["Items"].append(worry)
            m["Items"].pop(0)
            inspects[i] += 1

def task1():
    """ Task 1 solver """
    monkeys = deepcopy(inp_m)
    inspects = [0 for x in range(len(monkeys))]
    for i in range(20):
        throws(monkeys, inspects, 1)
    inspects.sort()
    return inspects[-1]*inspects[-2]

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    monkeys = deepcopy(inp_m)
    inspects = [0 for x in range(len(monkeys))]
    supermod = 1
    for m in monkeys:
        supermod *= m["Test"]
    for m in monkeys:
        m["Supermod"] = supermod
    for i in range(10000):
        throws(monkeys, inspects, 2)
    inspects.sort()
    return inspects[-1]*inspects[-2]

print("Task 2:", task2())
