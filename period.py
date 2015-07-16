def failure(string):
        N = len(string)
        F = [0]*(N+1)
        j = 0
        for i in xrange(2,N+1):
                while j>0 and string[i-1] != string[j]:
                        j = F[j]
                if string[i-1] == string[j]:
                        j += 1
                F[i] = j

                if i%(i-F[i]) == 0:
                        k = i/(i-F[i])
                        if k > 1:
                                print i,k
        
inp = input()
for x in xrange(1,inp+1):
        print "Test case #"+str(x)
        raw_input()
        failure(raw_input())
        print
