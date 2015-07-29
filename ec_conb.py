for _ in xrange(input()):
        n = input()
        if n%2:
                print n
        else:
                print int(bin(n)[-1: 1: -1], 2)
