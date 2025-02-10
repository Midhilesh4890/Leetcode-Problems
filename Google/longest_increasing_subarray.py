# Given an array of size N, find the maximum length of non-decreasing subarray:
# [0 7 3 10 2 4 6 8 0 9 -20 4]
# ans = 4, [2 4 6 8]


def solve(nums):
    n = len(nums)
    if n == 0:
        return 0, []  # Return empty if the input array is empty

    max_length = 1
    res = 1  # Tracks the maximum length found
    start_idx = 0  # Start index of the longest subarray found
    temp_start = 0  # Temporary start index for the current sequence

    for right in range(1, n):
        if nums[right] >= nums[right - 1]:  # Maintain non-decreasing condition
            max_length += 1
        else:
            max_length = 1  # Reset length if sequence breaks
            temp_start = right  # Start new sequence

        if max_length > res:
            res = max_length
            start_idx = temp_start  # Update start index of the max sequence

    return res, nums[start_idx:start_idx + res]

# Example usage:
nums = [0, 7, 3, 10, 2, 4, 6, 8, 0, 9, -20, 4]
length, subarray = solve(nums)
print(f"Max Length: {length}")
print(f"Subarray: {subarray}")

def maxIncreasingSubWithChange(arr):
    n = len(arr)
    if n <= 1:
        return n

    # left[i] stores the maximum increasing subarray ending at index i
    left = [1] * n  
    # right[i] stores the maximum increasing subarray starting at index i
    right = [1] * n  

    # Calculate the longest increasing subarray ending at each index
    for pos in range(1, n):
        if arr[pos] >= arr[pos - 1]:
            left[pos] = left[pos - 1] + 1

    # Calculate the longest increasing subarray starting at each index
    for pos in range(n - 2, -1, -1):
        if arr[pos] <= arr[pos + 1]:
            right[pos] = right[pos + 1] + 1

    # Find the maximum length of the increasing subarray without modification
    max_res = max(left)

    # Consider modifying an element at position `pos` (excluding first and last element)
    for pos in range(1, n - 1):
        if arr[pos - 1] <= arr[pos + 1]:  # Check if merging is possible
            max_res = max(max_res, left[pos - 1] + right[pos + 1] + 1)

    # Consider modifying the first element
    max_res = max(max_res, right[1] + 1)

    # Consider modifying the last element
    max_res = max(max_res, left[n - 2] + 1)

    return max_res

# Example usage:
nums = [0, 7, 3, 10, 2, 4, 6, 8, 0, 9, -20, 4]
length = maxIncreasingSubWithChange(nums)
print(f"Max Length: {length}")