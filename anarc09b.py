from fractions import gcd

while True:
	W,H = map(int,raw_input().split())
	if W == 0 and H == 0:
		break
	if H > W:
		W,H = H,W
	HCF = gcd(W,H)
	w = W/HCF
	h = H/HCF
	print w*h
