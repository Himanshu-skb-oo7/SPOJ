from sys import stdin
from math import sqrt

test = int(stdin.readline())

while test:
	r1,r2,r3 = map(int,stdin.readline().split())
	print ("%.6f"%((r1*r2*r3)/(r2*r3+r1*r3+r1*r2+2*sqrt(r1*r2*r3*(r1+r2+r3)))))
	test -= 1
