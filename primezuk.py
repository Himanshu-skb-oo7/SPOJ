def biggest_prime_factor(n):
	if n <= 3:
		return n
		
	if n % 2 == 0:
		temp = biggest_prime_factor(n/2)
		if temp == n/2:
			return n/2
		else:
			return temp
			
	if n % 3 == 0:
		temp = biggest_prime_factor(n/3)
		if temp == n/3:
			return n/3
		else:
			return temp
			
	for i in range(5, int(n**0.5) + 1, 6):
		if n % i == 0:
			temp = biggest_prime_factor(n/i)
			if temp == n/i:
				return n/i
			else:
				return temp
		if n % (i + 2) == 0:
			temp = biggest_prime_factor(n/(i+2))
			if temp == n/(i+2):
				return n/(i+2)
			else:
				return temp
	return n

test = input()
j = 1

for j in range(test):
	
	k = input()
	l = raw_input().split()
	num = 1
	for i in l:
		num *= int(i)
	num += 1
	print "Case #"+str(j+1)+":",biggest_prime_factor(num)
