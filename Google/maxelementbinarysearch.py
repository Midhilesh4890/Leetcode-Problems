# Given an sorted array, find the maximum frequency of a number.
# Eg: [1,2,2,3,3,3,3,4,4,5,6] : Answer: 4 (3 is repeated 4 times).

from bisect import bisect_left, bisect_right

def bisect_left(nums, target, n):
	l, r = 0, n - 1
	leftmost = 0
	while l <= r:
		mid = l + r >> 1

		if nums[mid] == target:
			r = mid - 1
			leftmost = mid
		elif nums[mid] < target:
			l = mid + 1 

		else:

			r = mid - 1 

	return leftmost

def bisect_right(nums, target, n):

	l, r = 0, n - 1
	righmost = 0
	while l <= r:
		mid = l + r >> 1

		if nums[mid] == target:
			l = mid + 1
			rightmost = mid
		elif nums[mid] < target:
			l = mid + 1 

		else:
			r = mid - 1 

	return rightmost

def solve(nums):
	n = len(nums)
	res = 1
	count = 0
	i = 0
	while i < n:
		left = bisect_left(nums, nums[i], n)
		right = bisect_right(nums, nums[i], n)
		res = max(res, right - left + 1)
		i = right + 1
		count += 1
	return res, count

nums = [1,2,2,3,3,3,3,4,4,4,5,6]
print(solve(nums))