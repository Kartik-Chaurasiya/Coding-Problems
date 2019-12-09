
"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.

 In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates 

 and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3."""

a= [1, 2, 0]
x=filter(lambda x: x >= 0, a)
b= sorted(list(x))
print("Sorted array",b)
c = 0
l = len(b)
print("Length of string",l)
for i in range(l):
	if b[i]==c and i<l-1:
		c= c+1
	elif b[i]!=c and c<=l:
		print("First positive number",c)
		break
	elif i==l-1 :
		print("First positive number",i+1)
	