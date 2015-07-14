from math import sqrt
from sys import stdin

inp = map(int,stdin.read().split())
test = inp[0]

for i in xrange(test):
	sq = int(sqrt(inp[i+1]))
	
	if sq*sq == inp[i+1]:
		print "Case "+str(i+1)+": Yes"
	else:
		print "Case "+str(i+1)+": No"
