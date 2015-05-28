from sys import stdin
	
t = int(stdin.readline())

for _ in xrange(t):

	stdin.readline()
	size = int(stdin.readline())
	l = []
	M = 0	
	for i in xrange(size):
		l.append(int(stdin.readline()))
		if l[i] > M:
			M = l[i]

	bitSize = 1
	while M+1 > bitSize:
		bitSize *= 2
	bit = [0]*(bitSize)
	
	count = 0

	for j in range(size):
		i,s = l[j],0
		while i>0:
			s += bit[i]
			i -= i&-i
		count += j - s
		
		i = l[j]
		while i< bitSize:
			bit[i] += 1
			i += i&-i
	print count
