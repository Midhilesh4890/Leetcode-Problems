# You are given a sequence of positive integers sequence. Your goal is to divide this sequence into parts non-empty contiguous subsequences. Among these partssubsequences, the number of subsequences whose sum of elements is at least threshold will be called the score. Find the maximum score.


# sequence = [1, 4, 2, 8]
# parts = 3
# threshold = 6

# Output:
# 2


# sequence = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# parts = 5
# threshold = 2

# Output:
# 5

from functools import lru_cache


def max_score(sequence, parts, threshold):
    n = len(sequence)

    if parts > n:
        return 0

    @lru_cache(None)
    def dfs(index, remaining_parts):
        if remaining_parts == 0 and index == n:
            return 0
        if remaining_parts == 0 or index == n:
            return -float("inf")

        max_score = -float("inf")
        current_sum = 0

        for j in range(index, n):
            current_sum += sequence[j]
            current_score = 1 if current_sum >= threshold else 0
            next_score = dfs(j + 1, remaining_parts - 1)
            if next_score != -float("inf"):
                max_score = max(max_score, current_score + next_score)

        return max_score

    result = dfs(0, parts)
    return result

sequence = [1, 4, 2, 8]
parts = 3
threshold = 6

sequence = [3, 2, 5, 1, 6]
parts = 3
threshold = 5

print(max_score(sequence, parts, threshold))


from functools import lru_cache

def max_score(sequence, parts, threshold):
    n = len(sequence)
    
    if parts > n:
        return 0  # Impossible to partition into more parts than elements

    # DP table, initialized with -inf to represent uncomputed states
    dp = [[-float('inf')] * (parts + 1) for _ in range(n + 1)]
    
    # Base case: 0 elements, 0 partitions => 0 score
    dp[0][0] = 0

    for i in range(1, n + 1):  # Loop over elements
        for j in range(1, parts + 1):  # Loop over partitions
            current_sum = 0
            for k in range(i, 0, -1):  # Try different partition points
                current_sum += sequence[k - 1]
                score = 1 if current_sum >= threshold else 0
                dp[i][j] = max(dp[i][j], dp[k - 1][j - 1] + score)

    return dp[n][parts] if dp[n][parts] != -float("inf") else 0

# Example usage
sequence = [3, 2, 5, 1, 6]
parts = 3
threshold = 5
print(max_score(sequence, parts, threshold))  # Outputs the optimal score
