from sys import stdin

def karatsuba(x,y):

	len1 = len(x)
	len2 = len(y)

	if len1 <= 1000 or len2 <= 1000:
		return int(x)*int(y)

	if len1 > len2:
		y = y.rjust(len1,'0')
		l = len1
	else:
		x = x.rjust(len2,'0')
		l = len2

	mid = l/2
	x0 = x[:mid] 
	x1 = x[mid:]
	y0 = y[:mid]
	y1 = y[mid:]

	z0 = karatsuba(x0,y0)
	z2 = karatsuba(x1,y1)
	z1 = karatsuba(x0,y1)+karatsuba(x1,y0)

	return ((10**l)*z0 + (10**((l)/2))*z1 + z2)

test = int(stdin.readline())

for x in xrange(test):
	a,b = stdin.readline().split()
	print karatsuba(a,b)
