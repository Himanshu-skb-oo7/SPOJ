test = input()
while test:
	x,avg = map(int,raw_input().split())
	num = (avg-x)*(avg+x+3)
	print num/2
	test -= 1
