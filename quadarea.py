from math import sqrt
from sys import stdin

test = int(stdin.readline())
#output = []
while test:
	a,b,c,d = map(float,stdin.readline().split())
	print "%0.02f"%(sqrt((-a+b+c+d)*(a-b+c+d)*(a+b-c+d)*(a+b+c-d))/4)
	test -= 1
