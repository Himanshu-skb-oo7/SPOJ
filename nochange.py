inp = map(int,raw_input().split())
x,k,v = inp[0],inp[1],inp[2:]

for i in range(1,k):
        v[i] += v[i-1]
result = [True]
for i in range(1,x+1):
        result.append(False)

for i in range(k):
        for j in range(v[i],x+1):
                result[j] |= result[j-v[i]]

print "YES" if result[x] else "NO"
