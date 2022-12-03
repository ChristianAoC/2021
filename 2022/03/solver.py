""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    rucksacks = [[(ord(x)-96)%58 for x in line.strip()] for line in file_handle]

def compare(r_one, r_two, r_three=""):
    """ Compare rucksacks to search for duplicates """
    for first in sorted(r_one):
        for second in sorted(r_two):
            if first==second and r_three=="":
                return first
            for third in sorted(r_three):
                if first==third and second==third:
                    return first
    return 0

def task1():
    """ Task 1 solver """
    result = 0
    for r_s in rucksacks:
        result += compare(r_s[0:int(len(r_s)/2)], r_s[int(len(r_s)/2):len(r_s)])
    print(result)

task1()

def task2():
    """ Task 2 solver """
    i = 0
    result = 0
    while i < len(rucksacks):
        result += compare(rucksacks[i], rucksacks[i+1], rucksacks[i+2])
        i+=3
    print(result)

task2()
