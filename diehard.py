dp = [[[0,0,0] for i in xrange(1,1100)] for j in xrange(1,1100)]

def die_hard(H,A,state):
        if state == 0:
                H += 3
                A += 2
        elif state == 1:
                H -= 5
                A -= 10
        else:
                H -= 20
                A += 5

        if H <= 0 or A <= 0:
                return 0
        if dp[H][A][state]:
                return dp[H][A][state]

        if state == 0:
                dp[H][A][state] = max(die_hard(H,A,1), die_hard(H,A,2)) + 1
        if state == 1:
                dp[H][A][state] = max(die_hard(H,A,0), die_hard(H,A,2)) + 1
        if state == 2:
                dp[H][A][state] = max(die_hard(H,A,0), die_hard(H,A,1)) + 1
        return dp[H][A][state]

for _ in xrange(input()):
        H,A = map(int,raw_input().split())
        print max(die_hard(H,A,0),die_hard(H,A,1),die_hard(H,A,2))
