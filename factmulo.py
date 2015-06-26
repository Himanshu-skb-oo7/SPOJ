test = input()
while test:
	
	p,n = map(int,raw_input().split())
	x,sum = p,0
	
	while n>=x:
		sum += ((n/x)*(n+1))-(x*(n/x)*(n/x + 1))/2
		x = x*p
	
	print max(sum,0)
	test -= 1
