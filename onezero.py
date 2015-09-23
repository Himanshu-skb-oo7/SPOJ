from collections import deque

def BFS(num):
	start = 1
	queue = deque()
	queue.append(start)
	while queue:
		node = queue.popleft()
		new_node = node*10
		if not new_node%num:
			return new_node
		if not (new_node+1)%num:
			return new_node+1
		queue.append(new_node)
		queue.append(new_node+1)

for i in range(input()):
	num = input()
	print BFS(num) if num != 1 else '1'
