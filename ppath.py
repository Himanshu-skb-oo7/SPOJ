from collections import deque

def neighbors(num):

	digit = num%10
	for i in range(1,digit,2):
		new_num = 10*(num/10) + i
		#print new_num
		if is_prime[new_num]:
			yield new_num
	if digit&1:
		digit += 1
	for i in xrange(digit+1,10,2):
		new_num = 10*(num/10) + i
		#print new_num
		if is_prime[new_num]:
			yield new_num

	for i in xrange(0,10):
		new_num = (num/100)*100 + i*10 + num%10
		#print new_num
		if is_prime[new_num] and new_num != num:
			yield new_num

	for i in xrange(0,10):
		new_num = (num/1000)*1000 + i*100 + num%100
		#print new_num
		if is_prime[new_num] and new_num != num:
			yield new_num

	for i in xrange(1,10):
		new_num = i*1000 + num%1000
		#print new_num
		if is_prime[new_num] and new_num != num:
			yield new_num


def distance(start, end):
	if start == end:
		return 0
	level = {start : 0}
	visited = {start : True}
	queue = deque()
	queue.append(start)
	while queue:
		node = queue.popleft()
		for i in neighbors(node):
			if is_prime[i]:
				try:
					if visited[i]:
						pass
				except KeyError:
						if i in level:
							level[i] = min(1 + level[node],level[i])
						else:
							level[i] = 1 + level[node]
						visited[i] = True
						if i == end:
							return level[end]
						queue.append(i)
	return -1

is_prime = [True]*10000
is_prime[0] = False
is_prime[1] = False

for i in xrange(2,100):
	if is_prime[i]:
		for j in xrange(i*i,10000,i):
			is_prime[j] = False
for _ in xrange(input()):
	start, end = map(int, raw_input().split())
	print distance(start, end)
