import time
import re

""" Advent of Code solver class """
startparse = time.time()
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]

p = []
a = []
b = []
for line in inp:
    resa = re.match(r"Button A: X\+(\d+), Y\+(\d+)", line)
    resb = re.match(r"Button B: X\+(\d+), Y\+(\d+)", line)
    resp = re.match(r"Prize: X=(\d+), Y=(\d+)", line)
    if resa:
        a.append((int(resa[1]), int(resa[2])))
    elif resb:
        b.append((int(resb[1]), int(resb[2])))
    elif resp:
        p.append((int(resp[1]), int(resp[2])))

endparse = time.time()
print(f"Parsing took {(endparse-startparse)*10**3:.03f}ms")

def task1():
    """ Task 1 solver """
    costs = []
    maxcost = 10000000000
    maxiter = 100
    for i in range(len(p)):
        costs.append({"cost": maxcost, "one": maxiter, "two": maxiter})
        for two in range(maxiter):
            for one in range(maxiter):
                if two*b[i][0] + one*a[i][0] == p[i][0] and two*b[i][1] + one*a[i][1] == p[i][1]:
                    if costs[i]["cost"] > (two*1 + one*3):
                        costs[i]["cost"] = (two*1 + one*3)
                        costs[i]["one"] = one
                        costs[i]["two"] = two
    result = 0
    for cost in costs:
        if cost["cost"] != maxcost:
            result += cost["cost"]
    return result

start = time.time()
print("Task 1 result:", task1(), f" (time: {(time.time()-start)*10**3:.03f}ms)")

def task2():
    """ Task 2 solver """
    cost = 0
    newp = []
    for i in range(len(p)):
        newp.append((p[i][0]+10000000000000, p[i][1]+10000000000000))

    for i in range(len(newp)):
        costb = ( newp[i][0]*a[i][1] - newp[i][1]*a[i][0] ) / ( b[i][0]*a[i][1] - b[i][1]*a[i][0] )
        if costb.is_integer():
            costa = (newp[i][0] - b[i][0]*costb) / a[i][0]
            if costa.is_integer():
                cost += costb * 1 + costa * 3
    return int(cost)

start = time.time()
print("Task 2 result:", task2(), f" (time: {(time.time()-start)*10**3:.03f}ms)")
