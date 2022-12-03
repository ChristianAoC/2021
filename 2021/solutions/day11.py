input = [[int(y) for y in x] for x in open('inputs/11.txt').read().strip().split('\n')]

### TASK 1

def flash(flashed, x, y):
  if flashed[x][y] == False:
    flashed[x][y] = True
    for i in [x-1, x, x+1]:
      for j in [y-1, y, y+1]:
        if i>=0 and j>=0 and i<len(input) and j<len(input[0]) and (i!=x or j!=y):
          if input[i][j] == 9:
            input[i][j] = 0
            flashed = flash(flashed, i, j)
          elif input[i][j] != 0:
            input[i][j] += 1
  return flashed

def step():
  flashed = [[False for x in range(len(input[0]))] for y in range(len(input))]
  for i, line in enumerate(input):
    for j, char in enumerate(line):
      if char == 9:
        input[i][j] = 0
      else:
        input[i][j] += 1

  for i, line in enumerate(input):
    for j, char in enumerate(line):
      if char == 0:
        flashed = flash(flashed, i, j)
  count = 0
  for line in input:
    count += line.count(0)
  return count

steps = 100
flashes = 0
i = 0

while i < steps:
  flashes += step()
  i += 1

print(f"Task 1: {flashes} flashes")

## TASK 2

arraysize = len(input)*len(input[0])

while step() < arraysize:
  steps += 1

print(f"Task 2: {steps+1} steps until all flash")

"""
print(input[0])
print(input[1])
print(input[2])
print(input[3])
print(input[4])
print(input[5])
print(input[6])
print(input[7])
print(input[8])
print(input[9])
"""