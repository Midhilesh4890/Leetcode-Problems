# Find the total number of subsets of an array such that the LCM of elements in each subset is divisible by k.


# Constraints:
# size(arr) ≤ 10^5
# 1 ≤ arr[i] ≤ 10^9
# 1 ≤ k ≤ 10^9


# Input: arr = {1, 7, 3, 2, 5}, k = 7
# Output: 16


# Input: arr = {2, 3, 1, 6, 1}, k = 6
# Output: 20

from math import gcd

def lcm(x, y):
        return x * y // gcd(x, y)

def count_subsets_lcm_divisible_by_k(arr, K):
    N = len(arr)

    dp = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]

    def helper(n, current_lcm):
        if n == 0:
            return 1 if current_lcm % K == 0 else 0

        if dp[n][current_lcm % K] != -1:
            return dp[n][current_lcm % K]
            
        new_lcm = lcm(current_lcm, arr[n - 1])
    
        include = helper(n - 1, new_lcm)
        exclude = helper(n - 1, current_lcm)

        dp[n][current_lcm % K] = include + exclude

        return dp[n][current_lcm % K]

    return helper(N, 1)

if __name__ == "__main__":
    arr = [2, 3, 4]
    K = 6
    result = count_subsets_lcm_divisible_by_k(arr, K)
    print(result)


