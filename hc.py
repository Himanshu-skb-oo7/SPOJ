test = int(raw_input())

while test:
	n = int(raw_input())
	l,h = 0,0
	for i in xrange(n):
		if raw_input() == 'lxh':
			l += 1
		else:
			h += 1

	isEven = False
	if l%2 == 0:
		isEven = True
	
	if h == n:
		print 'hhb'
	elif l == n:
		if isEven:
			print 'hhb'
		else:
			print 'lxh'
	elif h == l:
		if n%4 == 0:
			print 'hhb'
		else:
			print 'lxh'
	else:
		if not isEven:
			print 'lxh'
		else:
			print 'hhb'
	test -= 1
