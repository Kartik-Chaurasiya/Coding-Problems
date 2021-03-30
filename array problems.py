
"""Write a program to reverse an array or string
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}"""
def reverse(arr1, start, end):
    while start <= end:
        arr1[start], arr1[end] = arr1[end], arr1[start]
        start += 1
        end -= 1
    return arr1
arr1 = [1, 2, 3, 4, 5]
end = len(arr1) - 1
# print(reverse(arr1, 0, end))
# print(arr1[::-1])                                       


'''Maximum and minimum of an array using minimum number of comparisons'''
def minmax(arr2):
    min = arr2[0]
    max = arr2[0]
    for x in arr2:
        if x<min:
            min = x
        elif x>max:
            max = x
    print("min: {}, max: {}".format(min, max))
arr2 = [10,2,-3,4,5]
# minmax(arr2)
# print("min: {}, max: {}".format(min(arr2), max(arr2)))

'''Kth smallest element
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.'''
def find_nth_min(arr3, n_min):
    for x in arr3: 
        count = 0
        for y in arr3:
            if x > y:
                count += 1
        if count == n_min and arr3[len(arr3) - 1] == x:
            return x
arr3 = [7, 10, 4, 3, 20, 15]
n_min = 3
print(find_nth_min(arr3, n_min))