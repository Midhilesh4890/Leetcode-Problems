def only_differs_by_insertion(s1, s2):
    # Split both strings into lists of words
    words1 = s1.split()
    words2 = s2.split()
    
    # If they are the same length then they can't differ by an insertion.
    if len(words1) == len(words2):
        return False
    
    # Determine which list is shorter (the original) and which is longer (with the extra phrase)
    if len(words1) > len(words2):
        words1, words2 = words2, words1  # swap so that words1 is the shorter
    
    # Find the common prefix.
    i = 0
    while i < len(words1) and words1[i] == words2[i]:
        i += 1
        
    # Find the common suffix.
    j = len(words1) - 1
    k = len(words2) - 1
    while j >= i and k >= i and words1[j] == words2[k]:
        j -= 1
        k -= 1
        
    # If the entire shorter string was matched (i > j), then the only difference
    # is the extra block of words (from index i to k in the longer string).
    return i > j

# Test Examples
s1 = "The boy goes to the hospital"
s2 = "The cute little boy goes to the hospital"
print(only_differs_by_insertion(s1, s2))  # Should print True

s1 = "The boy is nice."
s2 = "The girl is nice."
print(only_differs_by_insertion(s1, s2))  # Should print False
