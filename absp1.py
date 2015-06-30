test = input()
output = ''

while test:
	
	size = input()
	x = raw_input().split()
	x[0] = int(x[0])
	ex = 0
	result = 0
	for i in xrange(size):
		just = int(x[i])-x[0]
		result += (i*just - ex)
		ex += just
	output += str(result)
	if test != 1:
		output += '\n'
	test -= 1
	
print output
