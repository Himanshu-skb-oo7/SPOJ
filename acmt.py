test = input()
for x in xrange(test):
        E,N = map(int,raw_input().split())
        if N > E:
                N,E = E,N
        if N == 0 or E == 0:
                print 0
        elif N > E/2:
                print (N+E)/3
        else:
                print N
