from sys import stdin

t = int(stdin.readline())

for _ in xrange(t):

    size = int(stdin.readline())
    yodaWords,expectedWords = [],[]
    
    yodaWords = stdin.readline().split()
    expectedWords = stdin.readline().split()
    
    l,dic = [],{}
    dic = dict(zip(yodaWords,[i+1 for i in xrange(size)]))
    
    for word in expectedWords:
        l.append(dic[word])

    bitSize = 1
    while size+1 > bitSize:
        bitSize *= 2

    bit = [0]*(bitSize)
    count,j = 0,0

    while j < size:
        i,s = l[j],0
        while i > 0:
            s += bit[i]
            i -= i&-i
        count += j-s

        i = l[j]
        while i < bitSize:
            bit[i] += 1
            i += i&-i
    	j += 1

    print count
