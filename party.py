from sys import stdin

def knapSack(S,size,values,n):

	K = [[0 for i in range(S+1)]for j in range(n+1)]
	fees = 0
	for i in xrange(1,n+1):
		for j in xrange(1,S+1):
			if size[i-1] <= j:
				K[i][j] = max(values[i-1]+K[i-1][j-size[i-1]],  K[i-1][j])
				#fees = j
			else:
				K[i][j] = K[i-1][j]
	# for i in xrange(1,n+1):
	# 	for j in xrange(1,S+1):
	# 		print K[i][j],
	# 	print
	fun = K[-1][-1]
	i,j = n,S
	while K[i][j] == fun:
		j -= 1

	print j+1,K[-1][-1]

while True:
	values,size = [],[]
	S,n = map(int,stdin.readline().split())
	if S == 0 and n == 0:
		break
	for _ in xrange(n):
		sz,val = map(int,stdin.readline().split())
		values.append(val)
		size.append(sz)
	knapSack(S,size,values,n)
	stdin.readline().split()
