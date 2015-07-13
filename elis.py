from sys import stdin
from math import sqrt

def LIS(numbers):

	n = len(numbers)
	result = [1 for _ in xrange(n)]
	
	for i in xrange(1,n):
		for j in xrange(0,i):
			if numbers[j]<numbers[i] and result[i] < result[j]+1:
				result[i] = result[j]+1
	return max(result)

stdin.readline()
sequence = map(int,stdin.readline().split())
print LIS(sequence)
