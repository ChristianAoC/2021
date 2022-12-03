input = [x for x in open('inputs/08.txt').read().strip().split('\n')]

### TASK 1

def count_1478():
  count = 0
  for line in input:
    for num in line.split(' | ')[1].split(' '):
      if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
        count += 1
  return count

#print("Task 1: "+str(count_1478()))

### TASK 2

codes = {
  'a': '',
  'b': '',
  'c': '',
  'd': '',
  'e': '',
  'f': '',
  'g': ''
}

temp = {
  'a': 'h',
  'b': 'i',
  'c': 'j',
  'd': 'k',
  'e': 'l',
  'f': 'm',
  'g': 'n'
}

numbers = {
  '0': '', # 6 - abcefg
  '1': '', # 2 - cf
  '2': '', # 5 - acdeg
  '3': '', # 5 - acdfg
  '4': '', # 4 - bcdf
  '5': '', # 5 - abdfg
  '6': '', # 6 - abdefg
  '7': '', # 3 - acf
  '8': '', # 7 - abcdefg
  '9': ''  # 6 - abcdfg
}

# 1, 4, 7, 8 are unique, so map those
def map_1478(line):
  for num in line.split(' '):
    if len(num) == 2:
      numbers['1'] = num
    elif len(num) == 3:
      numbers['7'] = num
    elif len(num) == 4:
      numbers['4'] = num
    elif len(num) == 7:
      numbers['8'] = num

# we know the diff between 1 and 7 is the "a" segment, map that
def map_a():
  for char in numbers['7']:
    if char not in numbers['1']:
      codes['a'] = char

# the 3 6-char numbers all have only 1 diff, but for 6 that is in 1 - giving us c
# we also know that the missing segment in 0 occurs in 4, so can deduce d and e
def map_cde(line):
  six = []
  diff = ""
  for num in line.split(' '):
    if len(num) == 6:
      six.append(num)
  for char in six[0]:
    if char not in six[1]:
      diff += char
  for char in six[1]:
    if char not in six[2]:
      diff += char
  for char in six[2]:
    if char not in six[0]:
      diff += char
  
  for char in diff:
    if char in numbers['1']:
      codes['c'] = char
      diff = diff.replace(char, '')
  
  for char in diff:
    if char in numbers['4']:
      codes['d'] = char
      diff = diff.replace(char, '')
  
  codes['e'] = diff

# once we know c, we can easily get f since it's the only other char in 1
def map_f():
  codes['f'] = numbers['1'].replace(codes['c'], '')

# only b and g missing at this point, check 4+8 to figure those out
def map_bg():
  for char in numbers['4']:
    if char not in codes.values():
      codes['b'] = char
  chars = 'abcdefg'
  for char in codes.values():
    chars = chars.replace(char, '')
  codes['g'] = chars

sum = 0

for line in input:
  for char in codes:
    codes[char] = ''
    
  map_1478(line)
  map_a()
  map_cde(line)
  map_f()
  map_bg()

  final = ""

  # we have all chars, let's do the replacement
  for num in line.split(' | ')[1].split(' '):
    if len(num) == 2:
      final += '1'
    elif len(num) == 3:
      final += '7'
    elif len(num) == 4:
      final += '4'
    elif len(num) == 7:
      final += '8'
    elif len(num) == 6:
      if codes['d'] not in num:
        final += '0'
      elif codes['c'] not in num:
        final += '6'
      else:
        final += '9'
    elif len(num) == 5:
      if codes['c'] not in num:
        final += '5'
      elif codes['f'] not in num:
        final += '2'
      else:
        final += '3'
  sum += int(final)

print(f"Task 2: {sum}")