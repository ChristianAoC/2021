from functools import lru_cache

### TASK 2

wins = {
  'p1': 0,
  'p2': 0
}

p1 = 4 #both example and real = 4
p2 = 8 #example = 8, real = 6
p1score = 0
p2score = 0
turn = 'p2'

def addwin(player):
  wins[player] += 1

@lru_cache(maxsize=None)
def play(p1, p2, p1score, p2score, turn):
  if p1score<21 and p2score<21:
    if turn == 'p1':
      turn = 'p2'
    else:
      turn = 'p1'
    for i in range(1, 4):
      for j in range(1, 4):
        for k in range(1, 4):
          if turn=='p1':
            play((p1+i+j+k-1)%10+1, p2, p1score+(p1+i+j+k-1)%10+1, p2score, turn)
          else:
            play(p1, (p2+i+j+k-1)%10+1, p1score, p2score+(p1+i+j+k-1)%10+1, turn)
  elif p1score>20:
    addwin('p1')
  else:
    addwin('p2')

play(p1, p2, p1score, p2score, turn)

print(wins['p1'])
print(wins['p2'])
print("Task 2: "+str(max(wins['p1'], wins['p2'])))
