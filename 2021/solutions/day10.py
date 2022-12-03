input = [x for x in open('../inputs/10.txt').read().strip().split('\n')]

### TASK 1

pairs = {
  "(" : ")",
  "[" : "]",
  "{" : "}",
  "<" : ">"
}

points1 = {
  ")" : 3,
  "]" : 57,
  "}" : 1197,
  ">" : 25137
}

sum1 = 0
newinput = []

def corrupt_check(line):
  opened = ""
  for i, char in enumerate(line):
    if char in pairs.keys():
      opened = char+opened
    elif char == pairs[opened[0]]:
      opened = opened[1:]
    else:
      return char

for line in input:
  if corrupt_check(line):
    sum1 += points1[corrupt_check(line)]
  else:
    newinput.append(line)

#print(sum1)

### TASK 2

points2 = {
  "(" : 1,
  "[" : 2,
  "{" : 3,
  "<" : 4
}

scores = []

def incomplete_check(line):
  opened = ""
  for i, char in enumerate(line):
    if char in pairs.keys():
      opened = char+opened
    elif char == pairs[opened[0]]:
      opened = opened[1:]
  return opened

for line in newinput:
  subsum = 0
  for char in incomplete_check(line):
    subsum = subsum*5+points2[char]
  scores.append(subsum)

print(sorted(scores)[int(len(scores)/2)])
