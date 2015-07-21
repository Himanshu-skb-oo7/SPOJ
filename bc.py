from math import log,ceil

for i in xrange(1,input()+1):
        N,M,K = map(int,raw_input().split())
        a = N*M*K-1
        b = ceil(log(M,2)) + ceil(log(N,2)) + ceil(log(K,2))
        print "Case #%d: %d %d" %(i,a,b)
