from sys import stdin
from math import sqrt

test = int(stdin.readline())
moves = [0,2]
for i in xrange(2,36):
	moves.append(3*moves[i-1]+2)
	
while test:
	print moves[int(stdin.readline())]
	test -= 1
