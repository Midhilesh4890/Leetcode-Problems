# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


#Method 1

from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)
    for i in range(m):
        substring = s2[i:i+n]
        if anagram(s1, substring):
            return True
    return False


def anagram(a,b):
    if len(a)!=len(b):
        return False
    return Counter(a) == Counter(b)


#Method 2 -- Lesser Wording

def checkInclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)
    c1 = Counter(s1)

    for i in range(m-n+1):
        c2 = Counter(s2[i:i+n])
        if c1 == c2:
            return True
    return False

