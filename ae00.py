x = input()
num = x
for i in range(2,int(x**0.5)+1):
	num += (x/i - i + 1)
print num
