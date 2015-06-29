test = input()

while test:
	n,m = raw_input().split()
	print int(str(int(n[::-1])+int(m[::-1]))[::-1])
	test -= 1
