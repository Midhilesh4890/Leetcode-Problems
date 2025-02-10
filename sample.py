# Consider a bank with some intial amount of money. Consider an array which represents list of transactions which are going to come through customers. + means deposit - means withdrawl. Bank can choose from which customer they want to start serving the customers and they can refuse any number of customers. But once they start they have to serve till the time its impossible to serve the customers. Maximize the amount_in_bank customers bank can serve.


# Example :
# Bank has 1 unit of money intially.
# Customer transactions : [1, -3, 5, -2, 1]


# answer = 3


def solve(amount_in_bank, nums):
    left, right = 0, 0 
    n = len(nums)
    customers = 0

    for right in range(n):
        amount_in_bank += nums[right]

        while amount_in_bank < 0 and left <= right:
            amount_in_bank -= nums[left]
            left += 1
        customers = max(customers, right - left + 1)

    return customers

nums = [1, -3, 5, -2, 1]
fund = 1

print(solve(fund, nums)) 


from typing import List, Set
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x


class Solution:
    def propertiesMerge(self, properties: List[List[str]]) -> List[Set[str]]:
        n = len(properties)
        uf = UnionFind(n)

        # property_group maps each "property"/"email" to the first index we saw it
        property_group = {}
        for i in range(n):
            property_size = len(properties[i])
            # properties[i][0] is the ID, properties[i][1..] are the properties
            for j in range(1, property_size):
                email = properties[i][j]
                if email not in property_group:
                    property_group[email] = i
                else:
                    uf.union(i, property_group[email])

        # Now we want to group by the final root parent
        # BUT we want sets of the *IDs* (i.e. properties[i][0]),
        # not [name, sortedEmails].
        
        root_to_ids = defaultdict(list)

        for i in range(n):
            root = uf.find(i)
            # Append this element's ID (the first field) into its root's list
            root_to_ids[root].append(properties[i][0])

        # Convert each list of IDs to a set
        result = []
        for _, ids in root_to_ids.items():
            result.append(set(ids))

        return result



# You are given a 2D grid grid of size m x n, where:

# Each cell contains a value of either 0 or 1.
# 0 represents water, which can either be saltwater (connected to the infinite ocean) or freshwater (completely surrounded by land).
# 1 represents land.
# The grid is implicitly surrounded by an infinite ocean of saltwater.
# You are also given a specific point [i, j] in the grid such that grid[i][j] == 1. 
# This point represents a land cell within a specific piece of land. 
# A piece of land is defined as a connected group of 1s (connected horizontally or vertically, but not diagonally).

# Your task is to determine the number of freshwater lakes within the piece of land that contains the cell [i, j]. 
# A freshwater lake is defined as a group of 0s that is completely enclosed by the land (i.e., not connected to the infinite ocean).

# Input:
# grid - A 2D integer array of size m x n (1 <= m, n <= 1000):
# grid[i][j] == 0 represents water.
# grid[i][j] == 1 represents land.
# [i, j] - A pair of integers representing a land cell's position in the grid, where grid[i][j] == 1.
# Output:
# An integer representing the number of freshwater lakes in the piece of land containing [i, j].

# Example:
# Input: grid = [
#     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#     [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0]
# ]
# point = [4, 4]
# Output: 2

"""
I am assuming that I'm given a particular "land" coordinate and have to find the lakes within that land body. The idea I'm using is to crop the array to find rectangular coordinates and then work on that.
Pad the sides with water and then fill the sea in this cropped array and then finally see the landlocked water bodies.
"""
import collections

arr = [
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def fillsea(image):
    ret = 0
    rows = len(image)
    cols = len(image[0])
    sea = set()
    q = collections.deque([(0, 0)])
    sea.add((0, 0))
    while q:
        x, y = q.popleft()
        for r, c in dirs:
            nr, nc = x + r, y + c
            if 0 <= nr < rows and 0 <= nc < cols and not image[nr][nc]:
                if (nr, nc) not in sea:
                    sea.add((nr, nc))
                    q.append((nr, nc))
    #lake = set()
    for x in range(rows):
        for y in range(cols):
            if not image[x][y] and (x, y) not in sea:
                q = collections.deque([(x, y)])
                sea.add((x, y))
                while q:
                    r, c = q.popleft()
                    for i, j in dirs:
                        nr, nc = r + i, j + c
                        if not image[nr][nc] and (nr, nc) not in sea:
                            sea.add((nr, nc))
                            q.append((nr, nc))
                ret += 1
    return ret
            

def countLakes(arr, tup):
    rows = len(arr)
    cols = len(arr[0])
    seen = set()
    seen.add(tup)
    x, y = tup
    q = collections.deque([(x, y)])
    while q:
        x, y = q.popleft()
        for r, c in dirs:
            nr, nc = x + r, y + c
            if 0 <= nr < rows and 0 <= nc < cols and arr[nr][nc]:
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc))

    minrow = rows
    maxrow = maxcol = 0
    mincol = cols
    #print(seen)

    for r, c in seen:
        minrow = min(minrow, r)
        maxrow = max(maxrow, r)
        mincol = min(mincol, c)
        maxcol = max(maxcol, c)

    image = [[0] + arr[i][mincol:maxcol + 1] + [0] for i in range(minrow, maxrow + 1)]
    l = len(image[0])
    image = [[0] * l] + image + [[0] * l]

    for i in range(len(image)):
        print(image[i])

    print(fillsea(image))

countLakes(arr, (2, 2))

Question 1:
You are given an array of length n and q queries. Each query consists of two indices [l, r], representing a subarray from index l to r (both inclusive). For each query, we are allowed to subtract 1 from any subsequence within the range [l, r]. After processing all the queries, determine whether it's possible to make all elements of the array equal to zero.


Example:
arr = [1, 2, 3]
queries = [[0, 1], [1, 2], [0, 2], [1, 2]]


Output: true


Explanation:
query --> arr -- subsequence
[0, 1] --> [0, 1, 3] -- {1, 2}
[1, 2] --> [0, 0, 2] -- {1 , 3}
[0, 2] --> [0, 0, 1] -- {2}
[1, 2] --> [0, 0, 0] -- {1}






