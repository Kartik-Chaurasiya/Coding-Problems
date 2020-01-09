n = 5
s=[1,2]
l=len(s)

def ways():
	while(l>0):
		for i in s:
		    sum=fibo(n+i-1)
		    l=l-1
		    return sum

def fibo(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return fibo(n-1)+fibo(n-2) 


count = ways()
print (count)
	