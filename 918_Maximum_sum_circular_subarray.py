# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

from collections import deque
#Brute Force Solution O(n^2)--> Gives TLE for bigger numbers
class Solution:
    def maxsubarray(self, nums):
        curr, maxsum = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr+nums[i])
            maxsum = max(curr, maxsum)
        return maxsum

    def maxSubarraySumCircular(self, nums):
        d = deque(nums)
        res = float('-inf')
        n = len(nums)+1
        while n > 0:
            d.rotate(-1)
            res = max(res, self.maxsubarray(d))
            n -= 1
        return res
#Kadane's Sign Variant algorithm
class Solution:
    def maxsubarray(self,nums):
        curr,maxsum = nums[0],nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i],curr+nums[i])
            maxsum = max(curr,maxsum)
        return maxsum
    
    def maxSubarraySumCircular(self,nums):
        k = self.maxsubarray(nums)
        #circularsum is total sum of nums + maxsubarraysum of nums in which its elements are multiplied by -1
        
        cs = sum(nums) + self.maxsubarray([-i for i in nums])
        
        return cs if cs>k and cs else k