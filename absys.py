for _ in range(input()):
	raw_input()
	l = raw_input().split()
	add = False
	mark = 0
	a = []
	for i in range(0,5,2):
		if "machula" in l[i]:
			mark = i
			if i==4:
				add = True
		else:
			a += [int(l[i])]
	if add:
		l[mark] = str(a[0]+a[1])
	else:
		l[mark] = str(a[1]-a[0])

	print ' '.join(l)
