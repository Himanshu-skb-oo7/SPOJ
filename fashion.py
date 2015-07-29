test = input()

for i in range(test):
	sum =0
	x = input()
	f = sorted(map(int,raw_input().split()))
	m = sorted(map(int,raw_input().split()))
	for i in range(x):
		sum += f[i]*m[i]
	print sum
