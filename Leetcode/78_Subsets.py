
# Given an integer array nums of unique elements, return all possible subsets(the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# Example 2:

# Input: nums = [0]
# Output: [[], [0]]

from itertools import chain, combinations

# Iterative
def subsets(nums):
    output = [[]]

    for i in nums:
        n = len(output)
        for j in range(n):
            result = output[j] + [i]
            output.append(result)
    return output


# Using Backtracking Approach

def subsets(nums):
    res = []
    subset = []

    def backtrack(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[i])
        backtrack(i+1)

        subset.pop()
        backtrack(i+1)

    backtrack(0)

    return res


#Using Itertools

def subsets(nums):
	return chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1))
