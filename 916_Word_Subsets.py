# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.


# Example 1:

# Input: words1 = ["amazon", "apple", "facebook", "google", "leetcode"], words2 = ["e", "o"]
# Output: ["facebook", "google", "leetcode"]
# Example 2:

# Input: words1 = ["amazon", "apple", "facebook", "google", "leetcode"], words2 = ["l", "e"]
# Output: ["apple", "google", "leetcode"]

from collections import Counter
def wordSubsets(words1,words2):
    words_count = Counter()
    for i in words2:
        words_count = words_count | Counter(i)
    return [i for i in words1 if len(words_count - Counter(i))==0]