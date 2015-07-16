test = input()

for _ in xrange(test):
        raw_input()
        n = input()
        badness = 0
        pos = []
        for rank in xrange(n):
                pos.append(int(raw_input().split()[-1]))

        pos = sorted(pos)
        #print pos
        for rank in xrange(n):
                badness += abs(rank+1-pos[rank])

        print badness
