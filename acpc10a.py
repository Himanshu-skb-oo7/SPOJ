while True:
	a,b,c = map(int,raw_input().split())
	if [a,b,c]== [0,0,0]:
		break
	if (2*b)==(a+c):
		print "AP",c+(b-a)
	elif b**2 == a*c:
		print "GP",c*(b/a)
