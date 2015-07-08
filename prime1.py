from math import sqrt
from sys import stdin

def getPrimes():
	primes = []
	isprime = [True]*32000
	isprime[0],isprime[1] = False,False

	for i in xrange(2,int(sqrt(32000))+1):
		if isprime[i]:
			for j in xrange(i*i,32000,i):
				isprime[j] = False

	for i in xrange(32000):
		if isprime[i]:
			primes.append(i)

	return primes

primes = getPrimes()
test = int(stdin.readline())
output = []

while test:
	m,n = map(int,stdin.readline().split())
	
	m = max(m,2)
	isprime = [True]*100001

	for i in primes:
		if i >= sqrt(n)+1:
			break
		if i >= m:
			first = i+i
		else:
			first = m+((i-m%i)%i)

		isprime[first-m:n+1-m:i] = [False]*len(isprime[first-m:n+1-m:i])

	for i in xrange(m,n+1):
		if isprime[i-m]:
			output.append(str(i))

	output.append('')
	test -= 1
print '\n'.join(output)
