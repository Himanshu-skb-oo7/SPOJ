for _ in range(input()):
        k,n,m = map(int,raw_input().split())
        
        if k == 1:
                if n%2 and m%2:
                        print '-'
                else:
                        print '+'
                continue
                
        MIN = min(n,m)
        if MIN%(k+1) == 0:
                print '+'
                continue
                
        if ((MIN/(k+1))%2):
                if (n+m)%2:
                        print '-'
                else:
                        print '+'
        else:
                if (n+m)%2:
                        print '+'
                else:
                        print '-'
