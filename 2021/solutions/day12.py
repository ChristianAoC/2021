input = [x for x in open('inputs/12.txt').read().strip().split('\n')]

### TASK 1

# split input into pairs and create lists of small and big caves
pairs = []
bigcaves = []
smallcaves = []

for pair in input:
  pairs.append(pair.split('-'))
  if pairs[-1][0] not in smallcaves and pairs[-1][0] not in bigcaves and pairs[-1][0] != "start" and pairs[-1][0] != "end":
    if pairs[-1][0].islower():
      smallcaves.append(pairs[-1][0])
    else:
      bigcaves.append(pairs[-1][0])
  if pairs[-1][1] not in smallcaves and pairs[-1][1] not in bigcaves and pairs[-1][1] != "start" and pairs[-1][1] != "end":
    if pairs[-1][1].islower():
      smallcaves.append(pairs[-1][1])
    else:
      bigcaves.append(pairs[-1][1])

# create dictionary to list all connections in waves in a proper way

ways = {
  "start": [],
  "end": []
}

for cave in smallcaves:
  ways[cave] = []
for cave in bigcaves:
  ways[cave] = []

for pair in pairs:
  if pair[1] not in ways[pair[0]] and pair[1] != "start":
    ways[pair[0]].append(pair[1])
  if pair[0] not in ways[pair[1]] and pair[0] != "start":
    ways[pair[1]].append(pair[0])

# function to recursively build all the paths
def search(path, cave):
  if cave not in smallcaves or path.find(','+cave) == -1:
    path += cave+","
    paths.append(path)
    for way in ways[cave]:
      if way != "end":
        search(path, way)
      else:
        paths.append(path+"end")

paths = []
path = ""
search(path, "start")

newpaths = []
for line in paths:
  if line[-1] != ',':
    newpaths.append(line)

print("Task 1: "+str(len(newpaths))+" distinct paths")

### TASK 2

# function to recursively build all the paths
def search2(path, cave):
  if cave not in smallcaves or path.find(','+cave) == -1:
    path += cave+","
  elif cave in smallcaves and path.find('2') == -1:
    path += cave+"2,"
  else:
    return
  paths.append(path)
  for way in ways[cave]:
    if way != "end":
      search2(path, way)
    else:
      paths.append(path+"end")

paths = []
path = ""
search2(path, "start")

newpaths = []
for line in paths:
  if line[-1] != ',':
    newpaths.append(line)

print("Task 2: "+str(len(newpaths))+" distinct paths")
