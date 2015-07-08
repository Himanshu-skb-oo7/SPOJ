from sys import stdin
from math import sqrt

test = int(stdin.readline())
final_output = []
while test:
	out = []
	N,K = map(int,stdin.readline().split())
	x = int((sqrt(1+8*N)-1)/2)
	m = x/K
	c = x%K
	just = (m*(m+1)*K)/2
	#print x,m,c
	i = 0 
	while i != c:
		i += 1
		out.append(str(just+i*(m+1)))
		#print out

	m -= 1
	i += 1
	just = (m*(m+1)*K)/2
	out.append(str(just+(N-(x*(x+1))/2)+i*(m+1))) 

	while i != K:
		i += 1
		out.append(str(just+i*(m+1)))
		
	for num in out:
		print num,
	print
	test -= 1
