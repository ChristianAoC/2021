""" Advent of Code solver class """
# A=X=Rock, B=Y=Paper, C=Z=Scissors
rps = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3 }

with open('sample.txt', 'r', encoding='utf8') as file_handle:
    aocinput = [[rps.get(x) for x in line.strip().split(' ')] for line in file_handle]

def task1():
    """ Task 1 solver """
    # calc game logic: match[0]-match[1]
    evalgame = { -2: 0, -1: 6, 0: 3, 1: 0, 2: 6 }
    score = 0
    for match in aocinput:
        score += evalgame[match[0]-match[1]]+match[1]
    print(score)

task1()

def task2():
    """ Task 2 solver """
    # X=lose, Y=draw, Z=win
    score = 0
    for match in aocinput:
        #score += match[1]%3 but then?
        if match[1]==1:
            score+=(match[0]+1)%3+1
        if match[1]==2:
            score+=3+match[0]
        if match[1]==3:
            score+=6+match[0]%3+1
    print(score)

task2()
