import re

""" Advent of Code solver class """
with open('sample2.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]

def task1(part_two = False):
    """ Task 1 solver """
    result = 0
    for line in inp:
        search = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        first = -1
        last = -1
        for i, k in enumerate(line):
            if k == 
            print("no"+k)
        #if part_two == True:
            #new_line = re.findall('|'.join(search), line)
            #print(new_line)
            #line = new_line
        #line = re.findall("\d+", line)
        #print(line)
        #line = int(line[0][0]+line[-1][-1])
        #result += line
    return result

print("Task 1:", task1(True))

def task2(part_two = False):
    """ Task 2 solver """
    result = 0
    for line in inp:
        if part_two == True:
            line = line.replace('one', '1')
            line = line.replace('two', '2')
            line = line.replace('three', '3')
            line = line.replace('four', '4')
            line = line.replace('five', '5')
            line = line.replace('six', '6')
            line = line.replace('seven', '7')
            line = line.replace('eight', '8')
            line = line.replace('nine', '9')
        line = re.findall("\d+", line)
        line = int(line[0][0]+line[-1][-1])
        result += line
    return result

print("Task 2:", task2(True))
