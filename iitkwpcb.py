def gcd(a,b):
	while b!=0:
        	a,b = b,a%b
	return a
test = input()
while test>0:
	x = input()
	j = x/2
	while j > 0:
		if gcd(x,j) == 1:
			break
		j -= 1
	print j
	test -= 1

