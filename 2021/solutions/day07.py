input = [int(x) for x in open('../inputs/07.txt').read().strip().split(',')]

### TASK 1

cost = 10000000
min = 0
max = 0

for crab in input:
  if crab < min:
    min = crab
  if crab > max:
    max = crab

i = min
while i < max:
  calc = 0
  for crab in input:
    calc += abs(i-crab)
  if calc < cost:
    cost = calc
  i += 1

print(cost)

### TASK 2

cost = 100000000000

i = min
while i < max:
  calc = 0
  for crab in input:
    calc += (abs(i-crab)*(abs(i-crab)+1))/2
  if calc < cost:
    cost = calc
  i += 1

print(cost)