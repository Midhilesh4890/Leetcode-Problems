# Given a binary array nums, return the maximum length of a contiguous subarray 
# with an equal number of 0 and 1.

#  Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


def findMaxLength(nums) -> int:
    nums = [-1 if val == 0 else val for val in nums]
    total = 0
    res = 0
    d = {}
    for i in range(len(nums)):
        total += nums[i]

        if total == 0:
            res = max(res, i+1)

        elif total in d:
            res = max(res, i-d[total])

        else:
            d[total] = i

    return res

