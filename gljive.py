import sys

l = []
s = 0
for i in range(10):
	l.append(int(sys.stdin.readline()))
	s += l[i]
	if s >= 100:
		if s-100 <= 100-s+l[i]:
			print (s)
			sys.exit(0)
		else:
			print (s-l[i])
			sys.exit(0)
print (s)
