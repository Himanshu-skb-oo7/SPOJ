for _ in xrange(input()):
        x,y,n = map(int,raw_input().split())
        ybit = bin(y)[2:]
        x = x%n
        result = 1
        for bit in ybit[::-1]:
                if bit == '1':
                        result = (result*x)%n
                x = (x*x)%n
        print result
