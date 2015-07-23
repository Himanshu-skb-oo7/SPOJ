def nCr(n,r):
        result = 1
        r = min(r,n-r)
        for i in xrange(1,r+1):
                result *= (n-r+i)
                result /= i
        return result%10000007

n,r = map(int,raw_input().split())
if r > n:
        print -1
elif n == r:
        print 1
else:
        print nCr(n-1,r-1)
