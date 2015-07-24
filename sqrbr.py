for _ in xrange(input()):
        n,k = map(int,raw_input().split())
        s = map(int,raw_input().split())
        
        dp = [[0 for i in xrange(50)] for j in xrange(50)]
        dp[1][1] = 1
        
        for i in xrange(2,2*n+1):
                for j in xrange(0,i+1):
                        if i in s:
                                dp[i][j] = dp[i-1][j-1]
                                if j == 0:
                                        dp[i][j] = 0
                        else:
                                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
                                if j == 0:
                                        dp[i][j] = dp[i-1][1]
        print dp[2*n][0]
