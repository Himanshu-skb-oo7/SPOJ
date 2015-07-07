for _ in range(input()):

	a,b,sum = map(int,raw_input().split())
	d = 0
	n = (sum*2)/(a+b)
	if n!= 5:
		d = (b-a)/(n-5)
	a1 = a -2*d
	s = str(a1)
	print n
	for k in range(2,n+1):
		if d!=0:
			s+= (" "+str(a1+(k-1))*d)
		else:
			s+=(" "+str(a1))
	print s
