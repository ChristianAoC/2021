input = [x for x in open('inputs/09.txt').read().strip().split('\n')]

### TASK 1

sum1 = 0

for i, line in enumerate(input):
  for j, point in enumerate(line):
    if j > 0 and line[j-1] <= point:
      pass
    elif j < len(line)-1 and line[j+1] <= point:
      pass
    elif i > 0 and input[i-1][j] <= point:
      pass
    elif i < len(input)-1 and input[i+1][j] <= point:
      pass
    else:
      sum1 += int(point)+1
      print(str(i)+","+str(j))

print(f"Task 1: {sum1}")

### TASK 2

basins = [0]*3
marked = [[0 for x in range(len(input[0]))] for y in range(len(input))] 

def basin_size(i, j):
  size = 0
  if j > 0 and input[i][j-1] != "9" and input[i][j-1] > input[i][j] and marked[i][j-1] == 0:
    size += 1+basin_size(i, j-1)
    marked[i][j-1] = "1"
  if j < len(input[i])-1 and input[i][j+1] != "9" and input[i][j+1] > input[i][j] and marked[i][j+1] == 0:
    size += 1+basin_size(i, j+1)
    marked[i][j+1] = "1"
  if i > 0 and input[i-1][j] != "9" and input[i-1][j] > input[i][j] and marked[i-1][j] == 0:
    size += 1+basin_size(i-1, j)
    marked[i-1][j] = "1"
  if i < len(input)-1 and input[i+1][j] != "9" and input[i+1][j] > input[i][j] and marked[i+1][j] == 0:
    size += 1+basin_size(i+1, j)
    marked[i+1][j] = "1"
  return size

for i, line in enumerate(input):
  for j, point in enumerate(line):
    if j > 0 and line[j-1] <= point:
      pass
    elif j < len(line)-1 and line[j+1] <= point:
      pass
    elif i > 0 and input[i-1][j] <= point:
      pass
    elif i < len(input)-1 and input[i+1][j] <= point:
      pass
    else:
      basin = basin_size(i, j)+1
      if basin > basins[0]:
        basins[2] = basins[1]
        basins[1] = basins[0]
        basins[0] = basin
      elif basin > basins[1]:
        basins[2] = basins[1]
        basins[1] = basin
      elif basin > basins[2]:
        basins[2] = basin

print("Task 2: "+str(basins[0]*basins[1]*basins[2]))
