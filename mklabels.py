i = 1
while True:
	n = input()
	if n == 0:
		break
	print "Case %d, N = %d, # of different labelings = %d"%(i,n,n**(n-2))
	i += 1	
