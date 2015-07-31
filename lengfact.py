from math import pi,floor,log as ln

def numDigits(n):
	if n==0 or n==1:
		return 1
	return floor((ln(2*pi*n)/2+n*(ln(n)-1))/ln(10))+1

for i in range(input()):
	print int(numDigits(input()))
