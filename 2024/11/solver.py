import time

""" Advent of Code solver class """
startparse = time.time()
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = file_handle.readline().strip()
#inp = "0 1 10 99 999" #sample 1
#inp = "125 17" #sample 2

endparse = time.time()
print(f"Parsing took {(endparse-startparse)*10**3:.03f}ms")

def blink(num):
    if num == "0":
        return "1"
    elif len(num) % 2 == 0:
        half = int(len(num)/2)
        newright = num[half:]
        while len(newright) > 1 and newright[:1] == "0":
            newright = newright[1:]
        return num[:half]+" "+newright
    else:
        return str(int(num) * 2024)

def task1():
    """ Task 1 solver """
    blinks = 25
    with open('input.txt', 'r', encoding='utf8') as file_handle:
        inp = file_handle.readline().strip()
    #inp = "0 1 10 99 999" #sample 1
    #inp = "125 17" #sample 2
    for _ in range(blinks):
        newinp = ""
        for num in inp.split():
            newinp += blink(num)+" "
        inp = newinp[:-1]
    return len(inp.split())

start = time.time()
print("Task 1 result:", task1(), f" (time: {(time.time()-start)*10**3:.03f}ms)")

def blinkInt(num):
    if num == 0:
        return [1]
    
    num = str(num)
    if len(num) % 2 == 0:
        half = int(len(num)/2)
        newright = num[half:]
        while len(newright) > 1 and newright[:1] == "0":
            newright = newright[1:]
        return [int(num[:half]), int(newright)]
    else:
        return [int(num) * 2024]

def addStone(stones, val, count):
    if val not in stones:
        stones[val] = count
    else:
        stones[val] += count
    return stones

def task2():
    """ Task 2 solver """
    with open('input.txt', 'r', encoding='utf8') as file_handle:
        inp = [int(x) for x in file_handle.readline().strip().split()]
    #inp = [x for x in "0 1 10 99 999".split()] #sample 1
    #inp = [x for x in "125 17".split()] #sample 2
    #print(inp)
    blinks = 75
    stones = {}
    for i in inp:
        addStone(stones, i, 1)
    for b in range(blinks):
        #print("Blink:", b)
        newstones = {}
        for _, num in enumerate(stones.copy().keys()):
            res = blinkInt(num)
            addStone(newstones, res[0], stones[num])
            if len(res) > 1:
                addStone(newstones, res[1], stones[num])
        stones = newstones
    return sum(stones.values())

start = time.time()
print("Task 2 result:", task2(), f" (time: {(time.time()-start)*10**3:.03f}ms)")
