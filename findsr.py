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

        if N%(N-F[N]) == 0:
                return N/(N-F[N])
        return 1

inp = raw_input()
while inp != '*':
        print failure(inp)
        inp = raw_input()
