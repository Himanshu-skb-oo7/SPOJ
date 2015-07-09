from sys import stdin
from math import log

while True:
	n = raw_input()#stdin.readline()
	if n == '00e0':
		break
	num = int(n[:2]+int(n[-1])*'0')
	result = 2*(num-2**int(log(num,2)))+1
	print result
