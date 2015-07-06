def sum_digits(n):
	sum = 0
	while n:
		sum += n%10
		n/=10
	return sum

test = input()
output = []
while test:
	num = input()
	s = sum_digits(num)

	while num%s != 0:
		num += 1
		ten = 0
		if num%10 == 0:
			ten = 1
			s = sum_digits(num)
		if ten == 0:
			s += 1
	print num
	test -= 1
