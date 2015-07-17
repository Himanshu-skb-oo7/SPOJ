for _ in xrange(input()):
        r,R = 0,0
        n = input()
        for i in xrange(n):
                x,y = map(int,raw_input().split())
                if x>r:
                        k = i+1
                        r = x
                elif y>R:
                        R = y
        if r > R:
                print k
        else:
                print -1
