test = input()

while test:
	a,b = map(int,raw_input().split())
	print min(b,3)+1-min(4,a)
	test -= 1
