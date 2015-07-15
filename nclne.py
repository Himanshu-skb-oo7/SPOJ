test = input()

for i in xrange(test):
        d = 1
        n,l = input(),map(int,raw_input().split())
        for j in xrange(n-1):
                d = (d-l[j])*2
        if d == l[n-1]:
                print "Yes"
        else:
                print "No"
