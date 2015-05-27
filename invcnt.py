from sys import stdin

def countInversion(l,first,last):
	if first >= last:
		return 0

	mid = (first+last)/2
	return countInversion(l,first,mid) + countInversion(l,mid+1,last) + mergeAndCount(l,first,mid,last)

def mergeAndCount(l,first,mid,last):
	i,j,k = first,mid+1,first
	count = 0
			
	while i <= mid and j <= last:
		if l[i] > l[j]:
			count += (mid-i+1)
			new[k] = l[j]
			j += 1
		else:
			new[k] = l[i]
			i += 1
		k += 1
	
	if j <= last:
		new[k:last+1] = l[j:last+1]
	else:
		new[k:last+1] = l[i:mid+1]
	
	l[first:last+1] = new[first:last+1]
	
	return count

t = int(stdin.readline())
for _ in xrange(t):

	blank = stdin.readline()
	size = int(stdin.readline())
	l = []
	new = [None for i in range(size)]
	
	for __ in xrange(size):
		l.append(int(stdin.readline()))
	
	print countInversion(l,0,size-1)
