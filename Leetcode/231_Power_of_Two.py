# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.


# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false


def isPowerOfTwo(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True

## Some background on bit
    #Every power of two will have only 1 and all zeors in its bit representation
    #and its number less than that will have one zero and all ones
    # For Example
    # 4 & 3 in bits -> 100 & 011 gives all zeros then 4 is a power of 2 and also n>0

def isPowerOfTwo(n):
    return n and (n&n-1) == 0
