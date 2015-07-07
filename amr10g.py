from sys import stdin

test = int(stdin.readline())
while test:
	
	N,K = map(int,stdin.readline().split())
	heights = list(map(int,stdin.readline().split()))

	heights = sorted(heights)
	MIN = 1000000000

	for i in xrange(N-K+1):
		if heights[i+K-1]-heights[i]<MIN:
			MIN = heights[i+K-1]-heights[i]

	print MIN
	test -= 1
