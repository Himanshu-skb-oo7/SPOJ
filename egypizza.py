test = input()
x,y,z,pizza = 0,0,0,1

while test:
	l = raw_input()
	
	if   l == '1/4':	x += 1
	elif l == '1/2':	y += 1
	elif l == '3/4':	z += 1
	
	test -= 1

pizza += min(x,z)
x -= (pizza - 1)
z -= (pizza - 1)
pizza += x/4
x = x%4
pizza += y/2
y = y%2

while x != 0 and z != 0:
	x -= 1
	z -= 1
	pizza += 1
	
while x != 0 and y != 0:
	if   x >= 2:
		x -= 2
		y -= 1
	elif x == 1:
		x -= 1
		y -= 1
	pizza += 1

if x:
	pizza += 1
if y:
	pizza += 1
if z:
	pizza += z
print pizza
