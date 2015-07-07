import math

while True:
	x = input()
	if x==-1:
		break
	y = math.sqrt(12*x-3)
	if y==int(y):
		print 'Y'
	else:
		print 'N'
