from sys import stdin

N,T = map(int,stdin.readline().split())#map(int,raw_input().split())

counter = [0 for i in xrange(7)]
dp = [[0 for i in xrange(1010)] for j in xrange(7)]
prices = [[-1 for i in xrange(110)] for j in xrange(7)]
quality = [[-1 for i in xrange(110)] for j in xrange(7)]

for i in xrange(N):
        items,p,q = map(int,stdin.readline().split())#map(int,raw_input().split())
        if items < 7 and items > 0:
                #counter[items] += 1
                prices[items][counter[items]] = p
                quality[items][counter[items]] = q
                counter[items] += 1
                

for i in xrange(1,T+1):
        dp[0][i] = float('inf')

for i in xrange(1,7):
        for j in xrange(1,T+1):
                dp[i][j] = dp[i][j-1]
                for k in xrange(counter[i]):
                        if j - prices[i][k] > 0:
                                dp[i][j] = max(dp[i][j],min(quality[i][k], dp[i-1][j-prices[i][k]]))

print dp[6][T]
