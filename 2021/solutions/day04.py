input = [x for x in open('inputs/04.txt').read().strip().split('\n')]

#### TASK 1

draw = input.pop(0).split(',')
input.pop(0)
bingo = []
board = []

for line in input:
  if line == '':
    bingo.append(board)
    board = []
  else:
    line = line.replace('  ', ' ').strip()
    board.append(line.split(' '))

def mark_bingo(arr, num):
  for i, board in enumerate(arr):
    for j, row in enumerate(board):
      for k, col in enumerate(row):
        if col == num:
          arr[i][j][k] = "x"
  return arr

def check_bingo(arr):
  for i, board in enumerate(arr):
    markedrows = [0, 0, 0, 0, 0]
    for j, row in enumerate(board):
      markedcols = 0
      for k, col in enumerate(row):
        if col == 'x':
          markedcols += 1
          markedrows[k] += 1
      if markedcols == 5:
        return i
    if 5 in markedrows:
      return i
  return -1

for value in draw:
  #bingo = [[["x" if k == value else None for k in j] for j in i] for i in bingo]
  mark_bingo(bingo, value)
  winner = check_bingo(bingo)
  if winner > 0:
    sum = 0
    for row in bingo[winner]:
      for col in row:
        if col[-1] != 'x':
          sum += int(col)
    bingo.pop(winner)
    print("Task 1: Winning score: "+str(int(value)*int(sum)))
    break

#print(bingo)

#### TASK 2

winningscore = 0

for value in draw:
  mark_bingo(bingo, value)
  winner = check_bingo(bingo)
  while winner > -1:
    sum = 0
    for row in bingo[winner]:
      for col in row:
        if col[-1] != 'x':
          sum += int(col)
    winningscore = int(sum)*int(value)
#    print("Bingo no: "+str(value)+" bingo board no: "+str(winner)+" sum of unmarked: "+str(sum))
#    print("Winning board:")
#    print("     "+' - '.join(bingo[winner][0]))
#    print("     "+' - '.join(bingo[winner][1]))
#    print("     "+' - '.join(bingo[winner][2]))
#    print("     "+' - '.join(bingo[winner][3]))
#    print("     "+' - '.join(bingo[winner][4]))
    bingo.pop(winner)
    winner = check_bingo(bingo)

print("Task 2: Winning score: "+str(winningscore))

print("Correct scores: 2745 and 6594")