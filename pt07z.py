from sys import stdin

test = int(stdin.readline())
graph = {i+1:[] for i in range(test)}

while test > 1:
    u,v = stdin.readline().split()
    u = int(u)
    v = int(v)
    graph[u].append(v)
    graph[v].append(u)
    test -= 1

level = {1:0}
i = 1
frontier = [1]
longestpath = 0
while frontier:
    next = []
    for u in frontier:
        for v in graph[u]:
            if v not in level:
                level[v] = i
                next.append(v)
            if level[u] > longestpath:
                longestpath = level[u]
                farthestvertex = u
        frontier = next
        i += 1
    
level = {farthestvertex:0}
i = 1
frontier = [farthestvertex]
longestpath = 0
while frontier:
    next = []
    for u in frontier:
        for v in graph[u]:
            if v not in level:
                level[v] = i
                next.append(v)
        if level[u] > longestpath:
                longestpath = level[u]
    frontier = next
    i += 1
    
print (longestpath)
