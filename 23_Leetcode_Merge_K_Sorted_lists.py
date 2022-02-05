# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: The linked-lists are:
# [
#     1 -> 4 -> 5,
#     1 -> 3 -> 4,
#     2 -> 6
# ]
# merging them into one sorted list:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.

# TC : O(N logK)
# SC : O(N)

from heapq import heappush,heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        heap = []
        for idx, element in enumerate(lists):
            if element:
                heappush(heap, (element.val, idx))
        dummy = curr = ListNode(0)
        while heap:

            val, idx = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heappush(heap, (lists[idx].val, idx))
        return dummy.next
