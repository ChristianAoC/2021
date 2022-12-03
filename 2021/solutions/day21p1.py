### TASK 1

d = {
  'p1': 4, #both example and real = 4
  'p2': 6, #example = 8, real = 6
  'p1score': 0,
  'p2score': 0,
  'dice': 0,
  'rolls': 0,
  'turn': 'p1'
}

def roll():
  d['dice'] += 1
  if d['dice']>100:
    d['dice'] = 1
  d['rolls'] += 1
  return d['rolls']

def play():
  d[d['turn']] += roll()+roll()+roll()
  d[d['turn']] = (d[d['turn']]-1)%10+1
  d[d['turn']+'score'] += d[d['turn']]
  if d['turn'] == 'p1':
    d['turn'] = 'p2'
  else:
    d['turn'] = 'p1'

while d['p1score']<1000 and d['p2score']<1000:
  play()

print("Task 1: "+str(min(d['p1score'], d['p2score'])*d['rolls']))
