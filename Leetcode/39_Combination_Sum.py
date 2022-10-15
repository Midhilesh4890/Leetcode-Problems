# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:

# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2, 3, 5], target = 8
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []


#Dp solution
def combinationSum(candidates,target):
    dp = [[] for _ in range(target+1)]

    for c in candidates:
        for i in range(0, target+1):
            if i < c:
                continue
            if i == c:
                dp[i].append([c])

            else:
                for j in dp[i-c]:
                    dp[i].append(j + [c])

    return dp[target]

#Recursion


class Solution:
    def combinationSum(self, candidates,target):
        self.res = []

        def recur(arr, output, total):
            if total == target:
                self.res.append(output)
            if total > target:
                return

            for i in range(len(arr)):
                recur(arr[i:], output + [arr[i]], total + arr[i])

        recur(candidates, [], 0)

        return self.res
