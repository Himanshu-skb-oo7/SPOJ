for i in range(input()):
	a,b = map(int,raw_input().split())
	if b%4==0 and b!=0:print (a**4)%10
	else:print (a**(b%4))%10
