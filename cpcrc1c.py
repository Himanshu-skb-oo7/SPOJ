def digitSum(num):
        if  num < 10:
                return (num*(num+1))/2
        
        tmp,i = num,0
        while tmp >= 10:
                i += 1
                tmp /= 10
        p = 10**i
        return ((tmp*45*i*p/10)+(tmp*(tmp-1)*p/2)+(tmp*(num%p+1))+digitSum(num%p))

while True:
        a,b = map(int,raw_input().split())
        if a == -1 and b == -1:
                break
        print digitSum(b) - digitSum(a-1)
