MOD = 1000000

def f(seed):
	seed = int(seed[3:6]+seed[0:3])
	target = (seed - 8964 + MOD)%MOD
	return "%06d" % target

while True:
	try:
		link = raw_input()
		guess = link[43:49]
		seed = link[37:43]
		target = f(seed)
		a,b = 0,0

		for i in range(6):
			if target[i] == guess[i]:
				a += 1
			for j in range(6):
				if guess[i] == target[j] and i != j:
					b += 1
		
		print "%dA%dB" %(countA, countB)
	except:
		break
