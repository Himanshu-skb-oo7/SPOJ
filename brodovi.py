#lot of optimization needed :((

from sys import stdin

inp = map(int,stdin.read().split())
N = inp[0]
l = inp[1:1+N]

check = [False]*(N)
result = 0

for i in xrange(1,N):
    if not check[i]:
        k = l[i]-1
        for j in xrange(i,N):
            if k == l[j]-1:
                check[j] = True
                k += l[i]-1
        result += 1
print result
