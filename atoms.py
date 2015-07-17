from math import log

for i in xrange(input()):
        n,k,m = map(int,raw_input().split())
        try:
            print int(log(m/n,k))
        except ValueError:
            print 0
