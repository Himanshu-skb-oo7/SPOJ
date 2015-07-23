from fractions import gcd

for i in xrange(input()):
        x,y,z= map(int,raw_input().split())
        if z>x and z>y:
                print "NO"
        else:
                g = gcd(x,y)
                if(z%g == 0):
                        print "YES"
                else:
                        print "NO"
