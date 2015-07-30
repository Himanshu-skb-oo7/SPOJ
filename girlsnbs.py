import math

while True:
	x,y = map(float,raw_input().split())
	
	if x == -1 and y == -1:
		break
	if y > x:
		x,y = y,x

	if x == 0 and y == 0:
		print 0
	elif x - y <2:
		print 1
	else:
		 print int((math.ceil(x/(y+1))))
