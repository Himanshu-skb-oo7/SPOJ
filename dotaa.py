from sys import stdin

test = int(raw_input())

while test:
	n,m,D = map(int,raw_input().split())
	ans = 0
	for x in xrange(n):
		num = int(raw_input())
		ans += (num - 1)/D
	if ans >= m:
		print 'YES'
	else:
		print 'NO'
 	test -= 1
