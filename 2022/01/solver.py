input = [line for line in open('input.txt', 'r')]

### TASK 1
most=0
sum=0
for cals in input:
	if cals!="\n":
		sum+=int(cals)
	else:
		if sum>most:
			most=sum
		sum=0

print(most)

### TASK 2
sums=[]
sum=0
for cals in input:
	if cals!="\n":
		sum+=int(cals)
	else:
		sums.append(sum)
		sum=0
sums.sort(reverse=True)

print(sums[0]+sums[1]+sums[2])