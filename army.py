for i in range(int(input())):
	input()
	input()
	l1 = list(map(int,input().split()))
	l2 = list(map(int,input().split()))

	print("Godzilla") if max(l1)>=max(l2) else print("MechaGodzilla")
