def base10toN(num,n):
	num_dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

	new_num_string=''
	current=num
	
	while current!=0:
		remainder=current%n
        	if 16>remainder>9:
            		remainder_string=num_dict[remainder]
        	elif remainder>=16:
            		remainder_string='('+str(remainder)+')'
        	else:
            		remainder_string=str(remainder)
        	
		new_num_string=remainder_string+new_num_string
        	current=current/n
    	return new_num_string

def baseNto10(num,n):
	no = 1
	num_dict = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
	new_num = 0
	for i in num[::-1]:
		if i<='9' and i>='0':
			new_num += int(i)*no
		else:
			new_num += num_dict[i]*no
		no *= n
	return new_num	
	
while True:
	try:
		l = raw_input()
		l = l.split()
		x = base10toN(baseNto10(l[0],int(l[1])),int(l[2]))
		if len(x)>7:
			x = "ERROR"
		print x.rjust(7)
	except:
		break
