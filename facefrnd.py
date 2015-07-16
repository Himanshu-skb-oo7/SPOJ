friends = set()
fof = set()
test = input()

for x in xrange(test):
        l  = list(map(int,raw_input().split()))
        friends.add(l[0])
        fof = fof.union(set(l[2:]))

print len(fof.difference(friends))
