def f(a,b):
        if a==min(a,b):
                a,b = b,a
        while b!=0:
                t = b
                b = a%b
                a = t
        return a

for i in range(input()):
        x,y,z = raw_input().split()
        gcd = f(int(x),int(y))
        print "Case",str(i+1)+":",
        if int(z)%gcd:
                print "No"
        else:
                print "Yes"
