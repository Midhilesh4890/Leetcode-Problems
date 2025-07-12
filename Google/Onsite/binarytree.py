# Given a binary tree (values are unique), and a vector of nums
# e.g.


#       0
#     /   \
#   1      2 
# /   \
# 3   4

# determine the nums is good or bad


# good: the nums position is sorted according to the inorder sequence
# bad: the nums position is not sorted according to the inorder sequence
# e.g.
# inorder of the tree = 3 1 4 0 2
# [1 4 2] -> good
# [3 1 0] -> good
# [3 4 1] -> bad because 4 is after 1 in inorder traversal sequence


# I kinda feel that I've seen the same problem in leetcode, anyone knows?


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root, inorder, index_map):
    if root:
        inorder_traversal(root.left, inorder, index_map)
        index_map[root.val] = len(inorder)  # Store index of value
        inorder.append(root.val)
        inorder_traversal(root.right, inorder, index_map)

def is_good_sequence(root, nums):
    inorder = []
    index_map = {}
    
    # Step 1: Perform inorder traversal & store indices
    inorder_traversal(root, inorder, index_map)
    
    # Step 2: Get the indices of nums in the inorder sequence
    inorder_indices = [index_map[num] for num in nums]
    
    # Step 3: Check if it's sorted
    return "good" if inorder_indices == sorted(inorder_indices) else "bad"

# Example Usage:
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

nums1 = [1, 4, 2]  # Good
nums2 = [3, 4, 1]  # Bad

print(is_good_sequence(root, nums1))  # Output: "good"
print(is_good_sequence(root, nums2))  # Output: "bad"


