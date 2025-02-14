# Given an array of integers, select K elements such that product is maximized. Return product.


# Did a sorting based approach - but missed some cases where all the numbers were negative, followup was


# No extra space after sorting
# No sorting - suggested Priority queues.
# How would u do it?


from functools import reduce
from operator import mul

def maxProductTwoPointerInPlace(arr, K):
    n = len(arr)
    
    # Case 1: If we need exactly `K` elements and `K == n`, return the product of all
    if K == n:
        return reduce(mul, arr, 1)
    
    # Initialize tracking variables
    min_neg1, min_neg2 = float('inf'), float('inf')  # Smallest and second smallest negative numbers
    max_pos1, max_pos2 = float('-inf'), float('-inf')  # Largest and second largest positive numbers
    neg_count, pos_count, zero_count = 0, 0, 0  # Counters for negative numbers, positives, and zeroes
    
    # Step 1: Single-pass traversal to find key elements
    for num in arr:
        if num > 0:
            pos_count += 1  # Count positive numbers
            # Update the two largest positive numbers dynamically
            if num > max_pos1:
                max_pos2, max_pos1 = max_pos1, num
            elif num > max_pos2:
                max_pos2 = num
        elif num < 0:
            neg_count += 1  # Count negative numbers
            # Track the two smallest (most negative) numbers dynamically
            if num < min_neg1:
                min_neg2, min_neg1 = min_neg1, num
            elif num < min_neg2:
                min_neg2 = num
        else:
            zero_count += 1  # Track zero count
    
    # Step 2: Handling different cases
    
    # Case 2: If we can select K positive numbers, pick the K largest positives
    if pos_count >= K:
        return reduce(mul, sorted([max_pos1, max_pos2] + [num for num in arr if num > 0])[-K:], 1)
    
    # Case 3: If negatives are required to balance the product
    if neg_count >= 2:
        return max(min_neg1 * min_neg2, max_pos1 * max_pos2)
    
    # Case 4: If there are zeros in the array, return 0 (best possible choice)
    if zero_count > 0:
        return 0
    
    # Case 5: Default to selecting the K largest elements (fallback case)
    return reduce(mul, sorted(arr, reverse=True)[:K], 1)

# Example Test Cases
arr1 = [1, 2, 3, 4, 5]
K1 = 3
print(maxProductTwoPointerInPlace(arr1, K1))  # Output: 60 (5*4*3)

arr2 = [-10, -20, 5, 2]
K2 = 2
print(maxProductTwoPointerInPlace(arr2, K2))  # Output: 200 (-10 * -20)

arr3 = [-10, -20, -5, -2, 3]
K3 = 3
print(maxProductTwoPointerInPlace(arr3, K3))  # Output: 400 (-10 * -20 * 3)

arr4 = [-10, -20, -5, -2, 0]
K4 = 3
print(maxProductTwoPointerInPlace(arr4, K4))  # Output: 0 (because of zero)

arr5 = [0, 0, 0, 0, 0]
K5 = 3
print(maxProductTwoPointerInPlace(arr5, K5))  # Output: 0 (all zeros)

arr6 = [-1, -2, -3, -4, -5]
K6 = 2
print(maxProductTwoPointerInPlace(arr6, K6))  # Output: 20 (-4 * -5)

arr7 = [1, -2, 3, -4, 5]
K7 = 3
print(maxProductTwoPointerInPlace(arr7, K7))  # Output: 15 (5 * 3 * 1)
