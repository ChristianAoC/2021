import numpy as np
input = [x for x in open('inputs/05.txt').read().strip().split('\n')]
vents = []

for line in input:
  vent = []
  for cloud in line.split(' -> '):
    vent.append(cloud.split(','))
  vents.append(vent)

map = np.full((1000, 1000), 0)

### TASK 1

def mark_vert(map_arr, coords):
  y1 = int(coords[0][1])
  y2 = int(coords[1][1])
  if y1 > y2:
    while y1 >= y2:
      map_arr[int(coords[0][0])][y2] += 1
      y2 += 1
  else:
    while y2 >= y1:
      map_arr[int(coords[0][0])][y1] += 1
      y1 += 1
  return map_arr

def mark_hori(map_arr, coords):
  x1 = int(coords[0][0])
  x2 = int(coords[1][0])
  if x1 > x2:
    while x1 >= x2:
      map_arr[x2][int(coords[1][1])] += 1
      x2 += 1
  else:
    while x2 >= x1:
      map_arr[x1][int(coords[1][1])] += 1
      x1 += 1
  return map_arr

for coords in vents:
  if coords[0][0] == coords[1][0]:
    map = mark_vert(map, coords)
  elif coords[0][1] == coords[1][1]:
    map = mark_hori(map, coords)

print("Task 1: "+str(np.count_nonzero(map > 1))) #7142

### TASK 2

def mark_diag(map_arr, coords):
  x1 = int(coords[0][0])
  x2 = int(coords[1][0])
  y1 = int(coords[0][1])
  y2 = int(coords[1][1])
  if x1 > x2 and y1 > y2:
    while x1 >= x2:
      map_arr[x2][y2] += 1
      x2 += 1
      y2 += 1
  elif x1 > x2 and y1 < y2:
    while x1 >= x2:
      map_arr[x1][y1] += 1
      x1 -= 1
      y1 += 1
  elif x1 < x2 and y1 > y2:
    while x1 <= x2:
      map_arr[x1][y1] += 1
      x1 += 1
      y1 -= 1
  elif x1 < x2 and y1 < y2:
    while x1 <= x2:
      map_arr[x1][y1] += 1
      x1 += 1
      y1 += 1
  return map_arr

for coords in vents:
  if coords[0][0] != coords[1][0] and coords[0][1] != coords[1][1]:
    map = mark_diag(map, coords)

print("Task 2: "+str(np.count_nonzero(map > 1))) #
