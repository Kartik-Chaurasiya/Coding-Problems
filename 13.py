s = "abcba"
ss = 2
l=list(s)
print(l)
list = []
size=len(l)
print(size)
a = l[0]
list.append(a)
i=1
while i<size and ss>0:
	for j in l :
		if ss > 0 :
			if a == j :
				list.clear()
				break
			elif a!=j and ss>0 :
				a = j
				list.append(j)
				ss = ss-1
		
	i = i+1

print (list)


