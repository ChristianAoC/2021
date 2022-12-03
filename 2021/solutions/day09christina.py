#fs = open(r"inputs/09.txt",'r')  
#ls = fs.readlines()
ls = [x for x in open('inputs/09.txt').read().strip().split('\n')]

sum_low_points = 0

# len(ls) returns 100 as expected
for x in range(len(ls)):
    #first line
    if x == 0:
        # len(ls[0]) incorrectly returns 101, probably because it counts the final \n as ls[0][100]
        for y in range(len(ls[0])):
            # first digit
            if y == 0:
                if int(ls[x][y]) < int(ls[x][y+1]) and int(ls[x][y]) < int(ls[x+1][y]):
                    sum_low_points += (int(ls[x][y])+1)
            # last digit
            elif y == (len(ls[0])-1):
                if int(ls[x][y]) < int(ls[x][y-1]) and int(ls[x][y]) < int(ls[x+1][y]):
                    sum_low_points += (int(ls[x][y])+1)
            else:
                if int(ls[x][y]) < int(ls[x][y-1]) and int(ls[x][y]) < int(ls[x+1][y]) and int(ls[x][y]) < int(ls[x][y+1]):
                    sum_low_points += (int(ls[x][y])+1)
                
    # last line
    elif x == (len(ls)-1):
        for y in range(len(ls[0])):
            # first digit
            if y == 0:
                if int(ls[x][y]) < int(ls[x-1][y]) and int(ls[x][y]) < int(ls[x][y+1]):
                    sum_low_points += (int(ls[x][y])+1)
            # last digit
            elif y == (len(ls[0])-1):
                if int(ls[x][y]) < int(ls[x][y-1]) and int(ls[x][y]) < int(ls[x-1][y]):
                    sum_low_points += (int(ls[x][y])+1)
            else:
                if int(ls[x][y]) < int(ls[x][y-1]) and int(ls[x][y]) < int(ls[x-1][y]) and int(ls[x][y]) < int(ls[x][y+1]):
                    sum_low_points += (int(ls[x][y])+1)

    else:
        for y in range(len(ls[0])):
            # first digit
            if y == 0:
                if int(ls[x][y]) < int(ls[x-1][y]) and int(ls[x][y]) < int(ls[x][y+1]) and int(ls[x][y]) < int(ls[x+1][y]):
                    sum_low_points += (int(ls[x][y])+1)
            # last digit
            elif y == (len(ls[0])-1):
                if int(ls[x][y]) < int(ls[x][y-1]) and int(ls[x][y]) < int(ls[x-1][y]) and int(ls[x][y]) < int(ls[x+1][y]):
                    sum_low_points += (int(ls[x][y])+1)
            else:
                if int(ls[x][y]) < int(ls[x][y-1]) and int(ls[x][y]) < int(ls[x-1][y]) and int(ls[x][y]) < int(ls[x][y+1]) and int(ls[x][y]) < int(ls[x+1][y]):
                    sum_low_points += (int(ls[x][y])+1)
        

print("Task 1: " + str(sum_low_points))
