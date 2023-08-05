
# You are given a string s containing one or more words. Every consecutive pair of words is separated by a single space ' '.

# A string t is an anagram of string s if the ith word of t is a permutation of the ith word of s.

# For example, "acb dfe" is an anagram of "abc def", but "def cab" and "adc bef" are not.
# Return the number of distinct anagrams of s. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: s = "too hot"
# Output: 18
# Explanation: Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".
# Example 2:

# Input: s = "aa"
# Output: 1
# Explanation: There is only one anagram possible for the given string.


class Solution:
    def anagrams(self, s):
        c = Counter(s)
        res = 1
        for num in c.values():
            res *= factorial(num)
            
        return factorial(len(s)) // res
        
    def countAnagrams(self, s):
        s = s.split(' ')
        total = 1
        for word in s:
            total *= self.anagrams(word) % (10 **9 + 7)
            
        return total % (10 ** 9 + 7)