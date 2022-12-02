input = [[x for x in line.strip().split(' ')] for line in open('input.txt', 'r')]

# A=X=Rock, B=Y=Paper, C=Z=Scissors
# 6=win, 3=draw, 0=loss
rps={
	'A': 1,
	'X': 1,
	'B': 2,
	'Y': 2,
	'C': 3,
	'Z': 3
}

# calc game logic: match[0]-match[1]
eval={
	-2: 0,
	-1: 6,
	0: 3,
	1: 0,
	2: 6
}

### TASK 1
score = 0
for match in input:
	score += eval[rps[match[0]]-rps[match[1]]]+rps[match[1]]
print(score)

### TASK 2
score = 0
# X=lose, Y=draw, Z=win
for match in input:
	if match[1]=='X':
		score+=(rps[match[0]]+1)%3+1
	if match[1]=='Y':
		score+=3+rps[match[0]]
	if match[1]=='Z':
		score+=6+rps[match[0]]%3+1

print(score)