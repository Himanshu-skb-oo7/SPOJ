dic = {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,0:0}
def is_happy(n):
	s = set()
	global counter
	counter = 0
	while (n > 1) and (n not in s):
    		s.add(n)
		counter += 1
    		n = sum(dic[int(d)] for d in str(n))
  	return n == 1

if is_happy(input()):
	print counter
else:
	print -1
