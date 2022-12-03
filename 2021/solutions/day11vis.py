#%%
#%matplotlib widget
import matplotlib.pyplot as plt
import matplotlib.animation as animation

input = [[int(y) for y in x] for x in open('../inputs/11.txt').read().strip().split('\n')]

def flash(flashed, x, y):
  if flashed[x][y] == False:
    flashed[x][y] = True
    for i in [x-1, x, x+1]:
      for j in [y-1, y, y+1]:
        if i>=0 and j>=0 and i<len(input) and j<len(input[0]) and (i!=x or j!=y):
          if input[i][j] == 9:
            input[i][j] = 0
            flashed = flash(flashed, i, j)
          elif input[i][j] != 0:
            input[i][j] += 1
  return flashed

def step():
  flashed = [[False for x in range(len(input[0]))] for y in range(len(input))]
  for i, line in enumerate(input):
    for j, char in enumerate(line):
      if char == 9:
        input[i][j] = 0
      else:
        input[i][j] += 1

  for i, line in enumerate(input):
    for j, char in enumerate(line):
      if char == 0:
        flashed = flash(flashed, i, j)
  count = 0
  for line in input:
    count += line.count(0)
  return count

totalflashes = 0
arraysize = len(input)*len(input[0])
steps = 0

fig = plt.figure()
im = plt.imshow(input, animated=True)
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

def updatefig(i):
  flashes = step()
#  steps += 1
#  totalflashes += flashes
#  ax.set_title("Step: "+str(i)+" | Flashes: "+str(flashes)+" | Total flashes: "+str(totalflashes))
  ax.set_title("Step: "+str(i)+" | Flashes: "+str(flashes))
  im.set_array(input)
  if flashes == arraysize:
    ani.event_source.stop()

ani = animation.FuncAnimation(fig, updatefig, interval=50)
plt.show()

#ani.save('day11.mp4', writer = 'ffmpeg', fps = 10)
