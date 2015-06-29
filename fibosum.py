from sys import stdin
import math
#from decimal import *

MOD = 1000000007

def fib(n):
	F = [[1,1],[1,0]]
	if n == 0:
		return 0
	
	power(F,n-1)
	return F[0][0]

def power(F,n):
	if n == 0 or n == 1:
		return
	
	M = [[1,1],[1,0]]
	power(F,n/2)
	multiply(F,F)
	
	if n%2 != 0: multiply(F,M)

def multiply(F,M):

	w =  (F[0][0]*M[0][0] + F[0][1]*M[1][0])%MOD;
	x =  (F[0][0]*M[0][1] + F[0][1]*M[1][1])%MOD;
	y =  (F[1][0]*M[0][0] + F[1][1]*M[1][0])%MOD;
	z =  (F[1][0]*M[0][1] + F[1][1]*M[1][1])%MOD;

	F[0][0] = w
	F[0][1] = x
	F[1][0] = y
	F[1][1] = z

test = int(stdin.readline())

for _ in xrange(test):
	N,M = map(int,stdin.readline().split())
	print ((fib(M+2)-fib(N+1)+MOD)%MOD)
