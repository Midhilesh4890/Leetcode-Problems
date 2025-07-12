# Find maximum length of a substring of a string with first charachter 
# lexicographically smaller than its last charachter.


# assume string length 10^5 char long, assume 26 small case english letters in string


# solve it in linear time.


# input : "dbabcb"
# output : 4


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        res = 0

        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                width = j - stack[-1]
                res = max(res, width)
                stack.pop()

        return res



        