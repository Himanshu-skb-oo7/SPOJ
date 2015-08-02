for i in range(input()):
	n,k = map(int,raw_input().split())
	n -= 1
	k -= 1
	k = min(k,n-k)
	ways = 1
	for i in range(1,k+1):
		ways *= (n-k+i)
		ways /= i
	print ways
