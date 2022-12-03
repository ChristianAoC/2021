from string import ascii_uppercase
input = [x for x in open('../inputs/14.txt').read().strip().split('\n')]

### TASK 1

template = input[0]
rules = {}
counts = {}

for line in input:
  if '->' in line:
    rules[line.split(' -> ')[0]] = line.split(' -> ')[1]
"""
def insertions(temp):
  newtemp = ""
  for i, char in enumerate(temp):
    if i == 0:
      newtemp += char
    else:
      newtemp += rules[temp[i-1]+char]+char
  return newtemp

def count_chars(temp):
  for char in ascii_uppercase:
    if temp.count(char) > 0:
      counts[char] = temp.count(char)

runs = 10
for i in range(runs):
  template = insertions(template)

count_chars(template)

print("Task 1: "+str(max(counts.values())-min(counts.values())))
"""
### TASK 2

counts.clear()
pairs = {}

for i, char in enumerate(input[0]):
  if i != 0:
    if input[0][i-1]+input[0][i] not in pairs:
      pairs[input[0][i-1]+input[0][i]] = 1
    else:
      pairs[input[0][i-1]+input[0][i]] += 1

def iterate_pairs():
  newpair = {}
  for pair, value in pairs.items():
    if pair[0]+rules[pair] not in newpair:
      newpair[pair[0]+rules[pair]] = value
    else:
      newpair[pair[0]+rules[pair]] += value
    if rules[pair]+pair[1] not in newpair:
      newpair[rules[pair]+pair[1]] = value
    else:
      newpair[rules[pair]+pair[1]] += value
  return newpair

def count_chars_in_pairs(pairs):
  counts[input[0][-1]] = 1
  for pair, value in pairs.items():
    if pair[0] not in counts:
      counts[pair[0]] = value
    else:
      counts[pair[0]] += value

runs = 40
for i in range(runs):
  pairs = iterate_pairs()

count_chars_in_pairs(pairs)

print("Task 2: "+str(max(counts.values())-min(counts.values())))
