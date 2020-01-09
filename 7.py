a=1234
a=str(a)
l=len(a)
print(l)
result = way(a,l)

def way(a, l):
	if a[0] == 0 :
		return 0;
	else :
		for i in range(l):
			sum = solve(a[i])+way(a[2:l])
