# K window of a list = distinct elements in the first K elements
# Given 2 lists, modify list2 such that the k windows of the 2 lists don't have any common element. Return the new list (Asked to optimize the space multiple times).


# Variation:
# Instead of 2 lists we have n lists, and a distance parameter d, the k window of a list shouldn't have any common element with any of the previous 'd' lists. Return the new lists

def modify_list2_in_place(list1, list2, K):
    S1 = set(list1[:K])
    
    # We'll use a pointer j to look for replacement candidates from list2[K:].
    j = K  
    # Iterate over the first K indices in list2.
    for i in range(K):
        if list2[i] in S1:
            # Look for a candidate from index j onward that is not in S1.
            while j < len(list2) and list2[j] in S1:
                j += 1
            if j < len(list2):
                # Swap the candidate into position i.
                list2[i], list2[j] = list2[j], list2[i]
                j += 1  # move j forward after using this candidate
            else:
                # No candidate available in the rest of list2.
                # Find a dummy value not in S1. (Here we choose the smallest positive integer not in S1.)
                dummy = 1
                while dummy in S1:
                    dummy += 1
                list2[i] = dummy
    return list2

# Example usage:
if __name__ == "__main__":
    # Example lists and window size.
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 3, 6, 7, 8, 9, 10]
    K = 3
    
    print("Original list1:", list1)
    print("Original list2:", list2)
    print("K window of list1:", set(list1[:K]))
    print("K window of list2 (before):", set(list2[:K]))
    
    modify_list2_in_place(list1, list2, K)
    
    print("\nModified list2:", list2)
    print("K window of list1:", set(list1[:K]))
    print("K window of list2 (after):", set(list2[:K]))
