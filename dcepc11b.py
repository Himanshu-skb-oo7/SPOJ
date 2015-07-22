for x in xrange(input()):
        n,p =  map(int,raw_input().split())
        if n >= p:
                print 0
                continue
        if n == 1:
                print 1
                continue
        if n == p-1:
                print p-1
                continue
        result = 1
        for i in xrange(n+1,p-1):
                result = (result*i)%p
        result = pow(result,p-2,p)
        print result
