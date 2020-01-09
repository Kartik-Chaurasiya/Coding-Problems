"""y = [10, 5, 2, 7, 8, 7]
k = 3
n = []
l = len(y)
l -=1
i=0
j=1
m=2
while(m<=l) :
	n.append(max(y[i], y[j], y[m]))
	i +=1
	j +=1
	m +=1
print(n)"""

"""This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)"""


# Python3 implementation of the approach 
# Function to print the maximum for 
# every k size sub-array 
def print_max(a, n, k): 
	
	# max_upto array stores the index 
	# upto which the maximum element is a[i] 
	# i.e. max(a[i], a[i + 1], ... a[max_upto[i]]) = a[i] 

	max_upto=[0 for i in range(n)] 

	# Update max_upto array similar to 
	# finding next greater element 
	s=[] 
	s.append(0) 

	for i in range(1,n): 
		while (len(s) > 0 and a[s[-1]] < a[i]): 
			max_upto[s[-1]] = i - 1
			del s[-1] 
		
		s.append(i) 

	while (len(s) > 0): 
		max_upto[s[-1]] = n - 1
		del s[-1] 

	j = 0
	for i in range(n - k + 1): 

		# j < i is to check whether the 
		# jth element is outside the window 
		while (j < i or max_upto[j] < i + k - 1): 
			j += 1
		print(a[j], end=" ") 
	print() 

# Driver code 

a =  [10, 5, 2, 7, 8, 7] 
n = len(a) 
k = 3
print_max(a, n, k) 

# This code is contributed by mohit kumar 



