manku = ['m','a','n','k','u']
for i in range(input()):
    num = input()
    x = num
    for i in range(1,26):
        z = 5**i
        if z >= x:
            break
        x -= z
    x -= 1
    y = ""
    for j in range(i):
        y = manku[x%5] + y
        x /= 5
    print y
