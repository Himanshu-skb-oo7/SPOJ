for _ in xrange(input()):
        num = input()
        tmp = float(num)
        result = 1.0
        while num > 1:
                num -= 1
                result += float((tmp/num))
        print "%.2f"%(result)
