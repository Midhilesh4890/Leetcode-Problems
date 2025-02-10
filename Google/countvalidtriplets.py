# You are given three sorted arrays A, B, and C, each of size n, and an integer D. The task is to count the number of unique tuples (i, j, k) where:


# i is an index in array A,
# j is an index in array B,
# k is an index in array C,
# such that the following conditions are satisfied:


# |A[i] - B[j]| ≤ D,  |A[i] - C[k]| ≤ D,  |B[j] - C[k]| ≤ D
# Input


# A, B, C: Lists of integers of length n, sorted in non-decreasing order.
# D: An integer representing the maximum allowable absolute difference.
# Output


# An integer representing the count of all valid tuples (i, j, k) that satisfy the conditions.


# Example


# Input:
# A = [0, 1]
# B = [0, 1]
# C = [0, 1]
# D = 1

# Output:
# 8
# Explanation:
# The following 8 tuples satisfy the conditions:


# (i=0, j=0, k=0), (i=0, j=0, k=1), (i=0, j=1, k=0), (i=0, j=1, k=1),
# (i=1, j=0, k=0), (i=1, j=0, k=1), (i=1, j=1, k=0), (i=1, j=1, k=1)
def count_valid_tuples(array_A, array_B, array_C, threshold_B, threshold_C, distance):
  
    left_B = 0
    right_B = 0
    left_C = 0
    right_C = 0
    valid_tuples_count = 0 

  
    for value_A in array_A:
        # Move left_B to the first position where B[left_B] + distance >= value_A
        while left_B < len(array_B) and array_B[left_B] + distance < value_A:
            left_B += 1

        # Move right_B to the first position where B[right_B] + threshold_B > value_A
        while right_B < len(array_B) and array_B[right_B] + threshold_B <= value_A:
            right_B += 1

        # Move left_C to the first position where C[left_C] + distance >= value_A
        while left_C < len(array_C) and array_C[left_C] + distance < value_A:
            left_C += 1

        # Move right_C to the first position where C[right_C] + threshold_C > value_A
        while right_C < len(array_C) and array_C[right_C] + threshold_C <= value_A:
            right_C += 1

  
        valid_tuples_count += (right_B - left_B) * (right_C - left_C)

    return valid_tuples_count  


def main():
    array_A = [
        1,
        2,
        3,
    ]
    array_B = [1, 2, 2]
    array_C = [1, 2, 3, 3]
    distance = 1  

    total_valid_tuples = (
        count_valid_tuples(array_A, array_B, array_C, 0, 0, distance)
        + count_valid_tuples(array_B, array_C, array_A, 0, 1, distance)
        + count_valid_tuples(array_C, array_A, array_B, 1, 1, distance)
    )

    print(total_valid_tuples)  


if __name__ == "__main__":
    main()