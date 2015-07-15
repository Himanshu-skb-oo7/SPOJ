from math import ceil

output = []
inp = input()
for i in xrange(inp):
        num = input()
        a = int(ceil((num-1)/5.0))
        if a == 0:
                output.append("poor conductor")
        else:
                if a%2 == 0:
                        b = 5*a-num+1
                        if b == 0:
                                output.append(str(a)+" W L")
                        if b == 1:
                                output.append(str(a)+" A L")
                        if b == 2:
                                output.append(str(a)+" A R")
                        if b == 3:
                                output.append(str(a)+" M R")
                        if b == 4:
                                output.append(str(a)+" W R")
                if a%2 == 1:
                        b = 5*a-num+1
                        if b == 0:
                                output.append(str(a)+" W R")
                        if b == 1:
                                output.append(str(a)+" M R")
                        if b == 2:
                                output.append(str(a)+" A R")
                        if b == 3:
                                output.append(str(a)+" A L")
                        if b == 4:
                                output.append(str(a)+" W L")
print '\n'.join(output)
