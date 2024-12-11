import time

""" Advent of Code solver class """
startparse = time.time()
with open('sample.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]

endparse = time.time()
print(f"Parsing took {(endparse-startparse)*10**3:.03f}ms")

def task1():
    """ Task 1 solver """
    result = 0
    return result

start = time.time()
print("Task 1 result:", task1(), f" (time: {(time.time()-start)*10**3:.03f}ms)")

def task2():
    """ Task 2 solver """
    result = 0
    return result

start = time.time()
print("Task 2 result:", task2(), f" (time: {(time.time()-start)*10**3:.03f}ms)")
