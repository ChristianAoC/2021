""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = file_handle.read().strip()

def task1():
    """ Task 1 solver """
    for i in range(0, len(inp)-3):
        ords = {char for char in inp[i:i+4]}
        if len(ords) == 4:
            return i+4

print(task1())

def task2():
    """ Task 2 solver """
    for i in range(0, len(inp)-13):
        ords = {char for char in inp[i:i+14]}
        if len(ords) == 14:
            return i+14

print(task2())
