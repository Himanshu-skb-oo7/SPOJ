from sys import stdin

def foo(num,k):
	result = str(num)+" "+str(k)+" "
	if num <= 1:
		return result+str(num)
	prev = 1
	for i in xrange(2,num+1):
		prev = ((prev+k-1)%i+1)
	result += str(prev)
	return result

output = []
while True:
	N,D = map(int,stdin.readline().split())
	if N == 0 and D == 0:
			break
	output.append(foo(N,D))
print '\n'.join(output)
