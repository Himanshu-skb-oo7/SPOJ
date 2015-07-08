from sys import stdin
from collections import defaultdict

wdic = defaultdict(int)
a = [0]

for i in xrange(1,500001):
	temp = a[i-1]-i
	if temp > 0 and not wdic[temp]:
		a.append(temp)
		wdic[temp] = True
	else:
		a.append(temp+i+i)
		wdic[temp+i+i] = True
#print a[500000]

while True:
	num = int(stdin.readline())
	if num == -1:
		break
	print a[num]
