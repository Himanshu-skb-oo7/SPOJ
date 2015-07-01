while True:
	x = raw_input()
	if x == '0':
		break
	x = x[::-1]
	l = [1,1]
	if x[0]=='0':
		l = [0,1]
	for i in xrange(1,len(x)-1):
		if x[i]=='0':
			l.insert(0,0)
		
		else:
			s = int(x[i]+x[i-1])
			if s<=26:
				l.insert(0,l[0]+l[1])
			else:
				l.insert(0,l[0])

	if int(x)<=9:
		print (1)
	elif int(x[len(x)-1]+x[len(x)-2])<=26:
		print l[0]+l[1]
	else:
		print l[0]
