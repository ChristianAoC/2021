import time
input = [int(x) for x in open('inputs/06.txt').read().strip().split(',')]

### TASK 1

def day_tick(fishes):
  new_fishes = 0
  for i, fish in enumerate(fishes):
    if fish == 0:
      fishes[i] = 6
      new_fishes += 1
    else:
      fishes[i] = fish-1
  i = 0
  while i < new_fishes:
    fishes.append(8)
    i += 1
  return fishes

i = 0
days = 18
while i < days:
#  input = day_tick(input)
  i += 1

#print(f"Task 1: {len(input)} fishes")

### TASK 1 - NEW

fish_counts = [0] * 9

for fish in input:
  fish_counts[fish] += 1

def day_tick2(fishes):
  new_fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i, fish in enumerate(fishes):
    if i == 0:
      new_fishes[0] = 0
      new_fishes[6] = fish
      new_fishes[8] = fish
    else:
      new_fishes[i-1] += fish
  return new_fishes

def sum_fishes(fishes):
  count = 0
  for fish in fishes:
    count += fish
  return count

days = 80
i = 0
while i < days:
  fish_counts = day_tick2(fish_counts)
  i += 1

print(f"Task 1: {sum_fishes(fish_counts)} fishes")


### TASK 2

start = time.time()

fish_counts = [0] * 9

for fish in input:
  fish_counts[fish] += 1

days = 256
i = 0
while i < days:
  fish_counts = day_tick2(fish_counts)
  i += 1

end = time.time()

print(f"Task 2: {sum_fishes(fish_counts)} fishes")

print("The time of execution of above program is :", end-start)