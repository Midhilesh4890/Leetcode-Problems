# Given an array, return true or false.

# Condition:

# True -> If there exists a combination that sums to the 
# maximum element in the array without using the maximum element.

# False -> Otherwise.

# Example: [1,3,4,5,12]

# Answer: True.
def can_sum_to_max(arr):
    n = len(arr)
    if n < 2:
        return False
    
    target = max(arr)
    arr.remove(max_element)  # Exclude the max element
    
    # Using dynamic programming to check if a subset sum equals target
    dp = [False] * (target + 1)
    dp[0] = True  # Base case
    
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

# Example usage:
print(can_sum_to_max([1, 3, 4, 5, 12]))  # Output: True

from itertools import combinations

def get_all_sums(arr):
    sums = set()
    n = len(arr)
    for i in range(n + 1):
        for subset in combinations(arr, i):
            sums.add(sum(subset))
    return sums

def can_sum_to_max_meet_middle(arr):
    if len(arr) < 2:
        return False

    max_element = max(arr)
    arr.remove(max_element)

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    left_sums = get_all_sums(left_part)
    right_sums = get_all_sums(right_part)

    # Check if any sum from left + sum from right equals max_element
    for s in left_sums:
        if (max_element - s) in right_sums:
            return True

    return False

# Example usage:
print(can_sum_to_max_meet_middle([1, 3, 4, 5, 12]))  # Output: True
