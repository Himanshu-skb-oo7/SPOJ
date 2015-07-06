for i in range(input()):
	x = raw_input()
	l = len(x)
	m = n = l/2
	if l%2 == 0:
		n = m-1
	if x[:m] == x[l-1:n:-1]:
		print "YES"
	else:
		print "NO"		
