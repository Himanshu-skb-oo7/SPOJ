oops = "Error!"	

while True:
	try:
		identifier = raw_input()
		
		if identifier[0].isupper() or identifier[0] == '_':
			print oops
			continue
		
		size = len(identifier)
		isJava = False
		isCpp = False
		result = ''
		i = 0
		
		while i < size:
			
			if identifier[i] == '_':
				isCpp = True
				i += 1
				if isJava or i == size:
					result = oops
					break
				else:
					if identifier[i].islower():
						result += identifier[i].upper()
					else:
						result = oops
						break
			
			elif identifier[i].isupper():
				isJava = True
				if isCpp:
					result = oops
					break
				else:
					result += '_'+ identifier[i].lower()
			
			elif identifier[i].islower():
				result += identifier[i]
			
			else:
				result = oops
				break
			i += 1		
		
		print result
	
	except:
		break
