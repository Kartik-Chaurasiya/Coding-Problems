"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns
 the largest sum of non-adjacent numbers. Numbers can be 0 
 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we
 pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we
  pick 5 and 5.
  
"""

def sum(a) :
	sum1 = 0    #current belement is included
	sum2 = 0    #current element is excluded

	for i in a :
		sum21 = sum2 if sum2>sum1 else sum1

		sum1 = sum2 + i
		sum2 = sum21

	return (sum2 if sum2>sum1 else sum1)

a = [5,5,10,100,10,5]
print (sum(a))


