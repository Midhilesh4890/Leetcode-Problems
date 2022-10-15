# Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

# Example 1:

# Input:
# N = 7, X = 2
# Arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 4
# Explanation: 2 occurs 4 times in the
# given array.
# Example 2:

# Input:
# N = 7, X = 4
# Arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 0
# Explanation: 4 is not present in the
# given array.


# As the array is sorted we can find the left and right occurence of target element in O(Logn) time

from bisect import bisect_left, bisect_right
class Solution:
	def count(self, arr, n, x):
    
		return bisect_right(arr, x) - bisect_left(arr, x)


