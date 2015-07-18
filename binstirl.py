for _ in range(input()):
        n,m = map(int,raw_input().split())
        print 0 if (n-m)&((m-1)/2) else 1
