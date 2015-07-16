from math import sqrt

while True:
        v,h = map(int,raw_input().split())
        if v == -1 and h == -1:
                break
        print "%.6f"%((v/9.8)*sqrt((v*v)+(2*9.8*h)))
