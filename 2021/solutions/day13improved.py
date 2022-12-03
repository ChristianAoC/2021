from collections import defaultdict

input = [x for x in open('inputs/13.txt').read().strip().split('\n')]

### TASK 1

# put input into proper array
dots = []
folds = []
xmax, ymax = 0, 0
data = defaultdict(lambda: ".")

for line in input:
  if ',' in line:
    dots.append([int(x) for x in line.split(',')])
  elif 'fold' in line:
    folds.append([line.split('=')[0][-1], int(line.split('=')[1])])

# folding
def fold(xy, line):
  newdots = []
  if xy == "x":
    for dot in dots:
      if (min(dot[0], dot[0]-(dot[0]-line)*2), dot[1]) not in newdots:
        newdots.append((min(dot[0], dot[0]-(dot[0]-line)*2), dot[1]))
  if xy == "y":
    for dot in dots:
      if ((dot[0], min(dot[1]-(dot[1]-line)*2, dot[1]))) not in newdots:
        newdots.append((dot[0], min(dot[1], dot[1]-(dot[1]-line)*2)))
  return newdots

folded_once = fold(folds[0][0], folds[0][1])
print("Task 1: "+str(len(folded_once)))

### TASK 2

for line in folds:
  dots = fold(line[0], line[1])
  if line[0] == 'x': xmax = line[1]-1
  if line[0] == 'y': ymax = line[1]-1

for dot in dots:
  data[(dot[0],dot[1])] = "#"

print("Task 2:")
for j in range(ymax+1):
  string = ""
  for i in range(xmax+1):
    if data[(i, j)] == "#": string += "██"
    else: string += "  "
  print(string)
