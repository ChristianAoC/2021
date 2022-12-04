""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]

aoc=[]
for pair in inp:
    sets=[]
    for elf in pair.split(','):
        x, y = elf.split('-')
        x = int(x)
        y = int(y)
        part = []
        while x <= y:
            part.append(x)
            x += 1
        sets.append(set(part))
    aoc.append(sets)

def task1():
    """ Task 1 solver """
    result = 0
    for pair in aoc:
        if set(pair[0]).intersection(pair[1]) == pair[0] or set(pair[0]).intersection(pair[1]) == pair[1]:
            result += 1
    print(result)

task1()

def task2():
    """ Task 2 solver """
    result = 0
    for pair in aoc:
        if set(pair[0]).intersection(pair[1]) != set():
            result += 1
    print(result)

task2()
