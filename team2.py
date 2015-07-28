i = 0
while True:
        try:
                i += 1
                line = sorted(map(int,raw_input().split()))
                print "Case %d: %d"%(i,line[2]+line[3])
        except:
                break
