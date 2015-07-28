from math import sqrt

def factorize(num):
        factors,N = {},set()
        for i in xrange(2,int(sqrt(num))+1):
                if num%i == 0:
                        count = 0
                        while num%i == 0:
                                num/= i
                                count += 1
                        factors[i] = count
                        N.add(i)
        if num > 1:
                factors[num] = 1
                N.add(num)
        return factors,N
k = 1
while True:
        A,B = map(int,raw_input().split())
        if A == 0 and B == 0:
                break
        factorsA,tmp1 = factorize(A)
        factorsB,tmp2 = factorize(B)
        tmp = tmp1.union(tmp2)
        distance = 0
        for f in tmp:
                try:
                        a = factorsA[f]
                except KeyError:
                        a = 0
                try:
                        b = factorsB[f]
                except KeyError:
                        b = 0
                distance += abs(a-b)
        print str(k)+". "+str(len(tmp))+":"+str(distance)        
        k += 1
