def f(n):
	no = 5
	x = 0
	while True:
		x += n/no
		no *= 5
		if n < no:
			break
	return x
for i in range(input()):
	print(f(input()))
