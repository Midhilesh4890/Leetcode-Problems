# Given an integer array nums, return all the triplets[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []

def threeSum(nums):
    nums.sort()
    res = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1
        while l < r:
            threesum = a + nums[l] + nums[r]
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res
