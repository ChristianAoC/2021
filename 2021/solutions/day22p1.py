from collections import defaultdict
from operator import *

input = [x.strip() for x in open('../inputs/22.txt', 'r')]

inp = []

for i, line in enumerate(input):
  if i>19: #ignore everything after line 20 because that's over -50/50 and not p1
    break
  seq = {'toggle': line.split(' ')[0]}
  for axis in line.split(' ')[1].split(','):
    if axis[0]=='x':
      seq['xs'] = int(axis.replace('x=','').split('..')[0])
      seq['xe'] = int(axis.replace('x=','').split('..')[1])
    if axis[0]=='y':
      seq['ys'] = int(axis.replace('y=','').split('..')[0])
      seq['ye'] = int(axis.replace('y=','').split('..')[1])
    if axis[0]=='z':
      seq['zs'] = int(axis.replace('z=','').split('..')[0])
      seq['ze'] = int(axis.replace('z=','').split('..')[1])
  inp.append(seq)

### TASK 1

cube = defaultdict(lambda: 'off')

for line in inp:
  for i in range(line['xs'], line['xe']+1):
    for j in range(line['ys'], line['ye']+1):
      for k in range(line['zs'], line['ze']+1):
          cube[(i,j,k)] = line['toggle']

print(countOf(cube.values(), 'on'))
