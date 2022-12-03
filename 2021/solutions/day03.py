import math
input = [x for x in open('inputs/03.txt').read().strip().split('\n')]

#### TASK 1

ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in input:
  for i, check in enumerate(line):
    if check == "1":
      ones[i] += 1

gamma = ""
epsilon = ""

for num in ones:
  gamma += str(math.floor(num/500))
  epsilon += str(abs(int(math.floor(num/500))-1))

print("Task 1 power consumption: "+str(int(gamma, 2)*int(epsilon, 2)))

#### TASK 2

oxygen = input.copy()
co2 = input.copy()

def count_commons(arg, pos):
  counter = 0
  for line in arg:
    if line[pos] == "1":
      counter += 1
  return counter

loop = 0
while loop < 12:
  newoxygen = []
  common = 0
  if count_commons(oxygen, loop) >= len(oxygen)/2:
    common = 1
  for line in oxygen:
    if int(line[loop]) == int(common):
      newoxygen.append(line)
  oxygen = newoxygen
  if len(oxygen) == 1:
    loop = 12
  loop += 1

loop = 0
while loop < 12:
  newco2 = []
  common = 0
  if count_commons(co2, loop) >= len(co2)/2:
    common = 1
  for line in co2:
    if int(line[loop]) != int(common):
      newco2.append(line)
  co2 = newco2
  if len(co2) == 1:
    loop = 12
  loop += 1

print("Task 2 life support rating: "+str(int(oxygen[0].replace('\n', ''), 2)*int(co2[0].replace('\n', ''), 2)))
