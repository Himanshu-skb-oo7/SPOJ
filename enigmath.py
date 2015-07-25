def f(a,b):
	if a==min(a,b):
		a,b = b,a
	while b!=0:
		t = b
		b = a%b
		a = t
	return a
t = input()
for i in range(t):
	x,y = map(int,raw_input().split())
	z = f(x,y)
	print y/z,x/z
