""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = file_handle.read().strip()

def task1():
    """ Task 1 solver """
    i = 0
    while i < len(inp)-3:
        ords = set()
        for char in inp[i:i+4]:
            ords.add(char)
        if len(ords) == 4:
            print(i+4)
            break
        i += 1

task1()

def task2():
    """ Task 2 solver """
    i = 0
    while i < len(inp)-13:
        ords = set()
        for char in inp[i:i+14]:
            ords.add(char)
        if len(ords) == 14:
            print(i+14)
            break
        i += 1

task2()
