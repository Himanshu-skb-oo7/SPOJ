while True:
	x = raw_input()
	if x == '-1':
		break
	x = int(x)
	num = []
	sum = 0
	counter = 0
	for i in xrange(x):
		p = input()
		num.append(p)
		sum += p
	if sum%x == 0:
		y = sum/x
		for i in xrange(x):
			if num[i]>y:
				counter += (num[i]-y) 
	else:
		counter = -1
	print counter
