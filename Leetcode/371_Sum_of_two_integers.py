# Given two integers a and b, return the sum of the two integers without using the operators + and -.


# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5

def getSum(a,b):
    mask = 0xffffffff
    while b:
        a,b = a^b,(a&b)<<1
    return a&mask if b>0 else a


#Java Code

# class Solution {
#     public int getSum(int a, int b) {
#         while (b != 0){
#             int carry = (a & b) << 1
#             a = a ^ b
#             b = carry
#         }

#         return a
#     }

# }
