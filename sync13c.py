from sys import stdin

test = int(stdin.readline())

while test:
	c1,c2 = map(int,stdin.readline().split())
	if c1%2 == 1 and c2%2 == 1:
		print "Ramesh"
	else:
		print "Suresh"
	test -= 1
