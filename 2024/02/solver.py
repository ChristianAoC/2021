""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.split() for line in file_handle]

def task1():
    """ Task 1 solver """
    safe = 0
    diff = []
    min = 1
    max = 3
    for line in inp:
        diffline = []
        for i in range(len(line)-1):
            diffline.append(int(line[i+1])-int(line[i]))
        diff.append(diffline)
    for line in diff:
        if all(abs(e) >= min and abs(e) <= max for e in line):
            if all(e > 0 for e in line) or all(e < 0 for e in line):
                safe += 1
    return safe

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    safe = 0
    min = 1
    max = 3
    for orig in inp:
        for i in range(len(orig)):
            diffline = []
            line = orig.copy()
            line.pop(i)
            for i in range(len(line)-1):
                diffline.append(int(line[i+1])-int(line[i]))
            if all(abs(e) >= min and abs(e) <= max for e in diffline):
                if all(e > 0 for e in diffline) or all(e < 0 for e in diffline):
                    safe += 1
                    break
    return safe

print("Task 2:", task2())
