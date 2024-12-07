""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]
    eqs = []
    for line in inp:
        new = []
        new.append(int(line.split(":")[0]))
        for el in line.split(":")[1].strip().split(" "):
            new.append(int(el))
        eqs.append(new)

def solve(cur, i, eq):
    if i >= len(eq):
        return cur == eq[0]
    elif cur > eq[0]:
        return False
    else:
        return solve(cur*eq[i], i+1, eq) or solve(cur+eq[i], i+1, eq)

def task1():
    """ Task 1 solver """
    sum = 0
    for eq in eqs:
        if solve(eq[1], 2, eq):
            sum += eq[0]
        else:
            remaining.append(eq)
    return sum

remaining = []
task1 = task1()
print("Task 1:", task1)

def solve2(cur, i, eq):
    if i >= len(eq):
        return cur == eq[0]
    elif cur > eq[0]:
        return False
    else:
        return solve2(cur*eq[i], i+1, eq) or solve2(cur+eq[i], i+1, eq) or solve2(int(str(cur)+str(eq[i])), i+1, eq)

def task2():
    """ Task 2 solver """
    sum = 0
    for eq in remaining:
        if solve2(eq[1], 2, eq):
            sum += eq[0]
    return sum + task1

print("Task 2:", task2())
