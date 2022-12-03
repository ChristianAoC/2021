input = [x for x in open('inputs/13.txt').read().strip().split('\n')]

### TASK 1

# put input into proper array
dots = []
folds = []

for line in input:
  if ',' in line:
    dots.append([int(x) for x in line.split(',')])
  elif 'fold' in line:
    xy = line.split('=')[0][-1]
    fold = line.split('=')[1]
    folds.append([xy,fold])

def fold(xy, line):
  newdots = []
  if xy == "y":
    for dot in dots:
      if dot[1] > line:
        dot[1] -= (dot[1]-line)*2
      newdots.append(dot)
  elif xy == "x":
    for dot in dots:
      if dot[0] > line:
        dot[0] -= (dot[0]-line)*2
      newdots.append(dot)
  else:
    newdots = dots
  return newdots

def find_duplicates(arr):
  newarray = []
  for i in range(len(arr)):
    nodupe = True
    for j in range(i + 1, len(arr)):
      if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
        nodupe = False
    if nodupe:
      newarray.append(arr[i])
  return newarray

#newdots = fold(folds[0][0], int(folds[0][1]))
#newdots = find_duplicates(newdots)
#print("Task 1: "+len(newdots))

### TASK 2

def fold(xy, line):
  newdots = []
  if xy == "y":
    for dot in dots:
      if dot[1] > line:
        dot[1] -= (dot[1]-line)*2
      newdots.append(dot)
  elif xy == "x":
    for dot in dots:
      if dot[0] > line:
        dot[0] -= (dot[0]-line)*2
      newdots.append(dot)
  else:
    newdots = dots
  return newdots

newdots = []
for line in folds:
  newdots = fold(line[0], int(line[1]))

newdots = find_duplicates(newdots)
max = [0, 0]

for dot in newdots:
  if dot[0] > max[0]:
    max[0] = dot[0]
  if dot[1] > max[1]:
    max[1] = dot[1]

matrix = []
i = 0
j = 0
while i <= max[1]:
  line = ['.'] * (max[0]+1)
  matrix.append(line)
  i += 1

for dot in newdots:
  matrix[dot[1]][dot[0]] = "#"

for line in matrix:
  print(line)
