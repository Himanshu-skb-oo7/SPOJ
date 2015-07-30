while True:
	n=input()
	sum=0
	if n==0.00:
		break
	for k in range(2,1000):
		sum+=1.0/k
		if sum>n:
			break
	print k-1,"card(s)"
