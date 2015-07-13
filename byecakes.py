from sys import stdin
from math import ceil

while True:
	E,F,S,M,e,f,s,m = map(int,stdin.readline().split())
	if E == -1:
		break
	E_,F_,S_,M_ = E,F,S,M
	if E%e != 0:
		E_ += (e - E%e)
	if F%f != 0:
		F_ += (f - F%f)
	if S%s != 0:
		S_ += (s - S%s)
	if M%m != 0:
		M_ += (m - M%m)
	MAX = max(E_/e,F_/f,S_/s,M_/m)
	E_ = MAX*e-E
	F_ = MAX*f-F
	S_ = MAX*s-S
	M_ = MAX*m-M
	print E_,F_,S_,M_
