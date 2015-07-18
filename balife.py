from sys import stdin

inp = map(int,stdin.read().split())
index = 1                                 #input()
while True:
        n = inp[index-1]
        if n == -1:
                break
        
        processors = inp[index:index+n]   #map(int,raw_input().split())
        index += n+1
        tasks = sum(processors)
        
        if tasks%n:
                print -1
        else:
                tsk,m = tasks/n,0
                for i in range(n-1):
                        diff = processors[i]-tsk
                        processors[i+1] += diff
                        m = max(m,abs(diff))
                print m
