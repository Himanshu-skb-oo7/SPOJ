MOD = 1000000007
while True:
        a, b, c = map(int, raw_input().split())
        if a == b == c ==-1:
                break
        if c == 0:
                print a%MOD
        elif b == 0:
                print 1
        elif a%MOD == 0:
                print 0
        else:
                result1 = pow(b, c, MOD-1)
                print pow(a, result1, MOD)
