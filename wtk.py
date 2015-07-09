def foo(num):
	if num <= 1:
		return num

	josephus = [0,1]
	
	for i in xrange(2,num+1):
		josephus.append((josephus[i-1]+num-i)%i+1)

	return josephus[num]

test = input()
for _ in xrange(test):
	num = input()
	print foo(num)
