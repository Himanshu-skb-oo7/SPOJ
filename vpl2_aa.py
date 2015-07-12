from sys import stdin
from math import log

test = int(stdin.readline())
#stdin.readline()
out = []
for i in range(test):
	output = ["Scenario","#"+str(i+1)+":"]
	p0,p1,t,p = map(int,stdin.readline().split())
	#stdin.readline()
	output.append("%.2f"%(t*(log(p)-log(p0))/(log(p1)-log(p0))))
	out.append(" ".join(output))
	
print ('\n'.join(out))
