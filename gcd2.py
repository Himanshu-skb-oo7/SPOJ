def f(a,b):
	if a==min(a,b):
		a,b = b,a
	while b!=0:
		t = b
		b = a%b
		a = t
	return a
	
for i in range(int(input())):
	x,y = map(int,input().split())
	print(f(x,y))
