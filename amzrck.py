l = []
l.append(1)
l.append(2)
for i in range(2,44):
	l.append(l[i-1]+l[i-2])
for i in range(input()):
	print l[input()]
