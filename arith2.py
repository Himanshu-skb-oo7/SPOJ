for i in range(int(input())):
	input()
	l = input().split()
	oper = [l[i] for i in range(1,len(l)-2,2)]
	num = [int(l[i])  for i in range(0,len(l),2)]
	
	result = num[0]
	
	for j in range(len(oper)):
		if oper[j] == '+':
			result += num[j+1]
		elif oper[j] == '-':
			result -= num[j+1]
		elif oper[j] == '*':
			result *= num[j+1]
		else:
			result = int(result/num[j+1])
	print(result)
