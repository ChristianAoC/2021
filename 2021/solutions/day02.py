file = open("inputs/02.txt")
input = file.readlines()

#### TASK 1

horizontal = 0
depth = 0

for line in input:
  direction, count = line.split(' ')
  if direction == "forward":
    horizontal += int(count)
  elif direction == "down":
    depth += int(count)
  elif direction == "up":
    depth -= int(count)

print("Task 1: "+str(horizontal*depth))

#### TASK 2

horizontal = 0
depth = 0
aim = 0

for line in input:
  direction, count = line.split(' ')
  if direction == "forward":
    horizontal += int(count)
    depth += aim*int(count)
  elif direction == "down":
    aim += int(count)
  elif direction == "up":
    aim -= int(count)

print("Task 2: "+str(horizontal*depth))
