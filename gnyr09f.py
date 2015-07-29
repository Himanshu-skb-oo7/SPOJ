dp = {(1,0):2,(2,0):3,(2,1):1}

def get_count(n,k):
        if k >= n or k < 0:
                return 0
        try:
                return dp[(n,k)]
        except KeyError:
                dp[(n,k)] = get_count(n-1,k) + get_count(n-2,k) + get_count(n-1,k-1) - get_count(n-2,k-1)

        return dp[(n,k)]

for _ in xrange(input()):
        i,n,k = map(int,raw_input().split())
        print i,get_count(n,k)
