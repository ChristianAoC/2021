import re
""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = "".join([line.strip() for line in file_handle])

def task1():
    """ Task 1 solver """
    result = 0
    res = re.findall("mul\((\d+),(\d+)\)", inp)
    for a, b in res:
        result += int(a) * int(b)
    return result

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    # last line needs a do() to be caught, and don't forget ? not greedy operator
    inp3 = re.sub("don't\(\).*?do\(\)", "", inp+"do()")
    # smarter:
    #inp3 = re.sub("don't\(\).*?(?:$|do\(\))", "", inp)
    result = 0
    res = re.findall("mul\((\d+),(\d+)\)", inp3)
    for a, b in res:
        result += int(a) * int(b)
    return result

print("Task 2:", task2())
