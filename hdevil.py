from math import sqrt

def fibonacci():
	fibo = [0,1]
	while True:
		fibo.append(fibo[-1]+fibo[-2])
		if fibo[-1] == 89:
			break
	return fibo

def factors(n):
	if n != 0: 
		return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))
	return set([1])
	
test = input()
fibo = fibonacci()

for i in xrange(test):
	n,m = map(int,raw_input().split())
	if (len(factors((sum(factors(n))-n)%m))-1) in fibo:
		print "Case #"+str(i+1)+ " : YES."
	else:
		print "Case #"+str(i+1)+ " : NO."
