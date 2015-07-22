for _ in xrange(input()):
        S = []
        R,C = map(int,raw_input().split())
        for i in xrange(R):
                S.append(map(int,raw_input().split()))

        dp = [[0 for i in xrange(C)] for j in xrange(R)]

        dp[R-1][C-1] = 1

        for i in xrange(C-2,-1,-1):
                if S[-1][i] >= dp[-1][i+1]:
                        dp[-1][i] = 1
                else:
                        dp[-1][i] = dp[-1][i+1] - S[-1][i]
        for i in xrange(R-2,-1,-1):
                if S[i][-1] >= dp[i+1][-1]:
                        dp[i][-1] = 1
                else:
                        dp[i][-1] = dp[i+1][-1] - S[i][-1]
        
        for i in xrange(R-2,-1,-1):
                for j in xrange(C-2,-1,-1):
                        k = min(dp[i][j+1],dp[i+1][j])
                        if S[i][j] >= k:
                                dp[i][j] = 1
                        else:
                                dp[i][j] = k - S[i][j]

        print dp[0][0]          
