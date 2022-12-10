""" Advent of Code solver class """
from pprint import pprint
import math

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]

def check_signal(cycle, X):
    """ task 1 - calculate signal """
    signal = cycle * X
    if cycle % 40 == 20:
        return signal
    return 0

def draw(cycle, X, screen):
    """ task 2 - draw scren """
    row = math.floor(cycle/40)
    pos = (cycle - 1) % 40
    sprite = [X-1, X, X+1]
    if pos in sprite:
        screen[row] = screen[row][:pos] + "#" + screen[row][pos+1:]
    return screen

def solver():
    """ Solves both today """
    result = 0
    X = 1
    cycle = 0
    screen = []
    for i in range(0, 6):
        pixels = ""
        for j in range(0, 39):
            pixels += "."
        screen.append(pixels)
    for line in inp:
        cycle += 1
        screen = draw(cycle, X, screen)
        result += check_signal(cycle, X)
        if line == "noop":
            pass
        else:
            cycle += 1
            result += check_signal(cycle, X)
            screen = draw(cycle, X, screen)
            X += int(line.split()[1])
    print("Task 1:", result)
    pprint(screen)

solver()