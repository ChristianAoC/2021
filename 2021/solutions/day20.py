input = [x.strip() for x in open('inputs/20.txt', 'r')]

### TASK 1

iea = input[0]
img = input
img.pop(0)
img.pop(0)
countlit = 0

def decode(x, y, void):
  code = ""
  global countlit
  for j in range(y-1, y+2):
    for i in range(x-1, x+2):
      if i<0 or j<0 or i>=len(img[0]) or j>=len(img):
        code += void
      elif img[j][i]=='.':
        code += "0"
      else:
        code += "1"
  if iea[int(code, 2)]=="#":
    countlit += 1
  return iea[int(code, 2)]

def enhance(void='0'):
  newimg = []
  for j in range(-1, len(img)+1):
    newline = ""
    for i in range(-1, len(img[0])+1):
      newline += decode(i, j, void)
    newimg += [newline]
  return newimg

for i in range(50):
  countlit = 0
  if i%2==1:
    img = enhance('1')
  else:
    img = enhance()

print(f"Task 2: {countlit} pixels lit")
