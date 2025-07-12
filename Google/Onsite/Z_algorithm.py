# I was asked the following question in the online interview:


# Given 2 strings 'A' & 'B', find whether it is possible to cut both strings at a common point such that
# concatenating the first part of one string and the second part of the other string results in a palindrome.


# Example 1:
# Input: A = "abcdef" B = "xyzcba"
# Output: true -> as we can cut both the string from index 2 to get the palindromic string "abccba"


# Example 2:
# Input: A = "abcxxxdef" B = "abcabccba"
# Output: true -> as we can cut both the string from index 5 to get the palindromic string "abcxxxcba"


# Follow up question:


# Instead of cutting at the same point, you can now cut at different points (and
# do the same operation of concatenating first part of one string with the second part of the other).
# What is the length of the longest palindrome that can be formed this way?

class Solution:
    def longestPalindromeFormation(self, a: str, b: str) -> int:
        def z_function(s):
            """Computes the Z-array in O(N) time."""
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z

        n = len(a)
        a_rev, b_rev = a[::-1], b[::-1]

        # Compute Z-values for checking how much of `b` matches `a_rev`
        z1 = z_function(a_rev + "$" + b)  # How much of `b` matches `a_rev`
        z2 = z_function(b_rev + "$" + a)  # How much of `a` matches `b_rev`

        max_palindrome_length = 0

        # Iterate over all possible split points
        for i in range(n + 1):
            # Ensure we do not access an out-of-bounds index
            if n + 1 + i < len(z1):
                pal_len1 = i + z1[n + 1 + i]  # First i chars from a, rest from b
            else:
                pal_len1 = i

            if n + 1 + i < len(z2):
                pal_len2 = i + z2[n + 1 + i]  # First i chars from b, rest from a
            else:
                pal_len2 = i

            max_palindrome_length = max(max_palindrome_length, pal_len1, pal_len2)

        return max_palindrome_length

# Test cases
test_cases = [
    ("abc", "cba", 6),
    ("x", "y", 1),
    ("xbdef", "xecab", 3),
    ("ulacfd", "jizalu", 7),
    ("racecar", "racecar", 7),
    ("a" * 10**5, "b" * 10**5, 1),
    ("aabb", "bbaa", 4)
]

# Running test cases
solution = Solution()
for i, (a, b, expected) in enumerate(test_cases, 1):
    output = solution.longestPalindromeFormation(a, b)
    print(f"Test {i}: {'PASS' if output == expected else 'FAIL'} (Expected {expected}, Got {output})")

print('##############################################################')
class Solution:
    # Helper function to compute LPS array for KMP
    def compute_lps(self, s):
        n = len(s)
        lps = [0] * n
        j = 0  # Length of previous longest prefix suffix
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j
        return lps

    def longestPalindromeFormation(self, a: str, b: str) -> int:
        n = len(a)
        a_rev = a[::-1]
        b_rev = b[::-1]

        # Compute LPS for reversed strings concatenated with the other string
        lps1 = self.compute_lps(a_rev + "$" + b)
        lps2 = self.compute_lps(b_rev + "$" + a)

        max_palindrome_length = 0  # Track maximum palindrome length

        # Iterate over all possible split points
        for i in range(n + 1):
            # Check palindrome length for both combinations
            pal_len1 = i + (lps1[n + 1 + i] if n + 1 + i < len(lps1) else 0)
            pal_len2 = i + (lps2[n + 1 + i] if n + 1 + i < len(lps2) else 0)

            # Update maximum palindrome length
            max_palindrome_length = max(max_palindrome_length, pal_len1, pal_len2)

        return max_palindrome_length

# Test cases for Part 2
solution = Solution()
print(solution.longestPalindromeFormation("abc", "cba"))        # Output: 6
print(solution.longestPalindromeFormation("x", "y"))            # Output: 1
print(solution.longestPalindromeFormation("xbdef", "xecab"))    # Output: 3
print(solution.longestPalindromeFormation("ulacfd", "jizalu"))  # Output: 7
print(solution.longestPalindromeFormation("racecar", "racecar"))# Output: 7
