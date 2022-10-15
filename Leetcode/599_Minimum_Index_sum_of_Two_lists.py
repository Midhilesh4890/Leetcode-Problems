# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.


# Example 1:

# Input: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"], list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:

# Input: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"], list2 = ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

import math,itertools

#O(n) with space
def findRestaurant(list1,list2):
    res = []
    d1 = {val: i for i, val in enumerate(list1)}
    d2 = {val: i for i, val in enumerate(list2)}
    common = d1.keys() & d2.keys()

    minindex = math.float('inf')

    for i in common:
        index_len = d1[i] + d2[i]
        if index_len < minindex:
            minindex = index_len
            res = [i]
        elif index_len == minindex:
            res.append(i)
    return res

#O(n^2) without space
def findRestaurant(list1,list2):
    minindex = math.float('inf')
    res = []
    for i, j in itertools.product(list1, list2):
        if i == j:
            index_len = list1.index(i) + list2.index(j)
            if index_len < minindex:
                minindex = index_len
                res = [i]
            elif index_len == minindex:
                res.append(i)
    return res
