test = input()
for i in range(test):
    x = raw_input().split()
    x[3] = int(x[3])
    ans = x[3] + (x[3]-int(x[0]))/(int(x[1])-1)
    print ans
