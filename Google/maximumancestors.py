class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_max_ancestor_for_leaves(root):
    if not root:
        return {}

    leaf_max_ancestor = {}

    def dfs(node, max_ancestor):
        if not node:
            return

        # Update the max ancestor for this path
        max_ancestor = max(max_ancestor, node.val)

        # If it's a leaf node, store the result
        if not node.left and not node.right:
            leaf_max_ancestor[node.val] = max_ancestor
            return

        # Continue DFS on left and right children
        dfs(node.left, max_ancestor)
        dfs(node.right, max_ancestor)

    dfs(root, float('-inf'))  # Start DFS with the smallest possible max
    return leaf_max_ancestor

# Constructing the example tree:
#         4
#       /   \
#      5     3
#     /     / \
#    1     2   6
root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.right.left = TreeNode(2)
root.right.right = TreeNode(6)

# Compute and print results
result = find_max_ancestor_for_leaves(root)
for leaf, max_ancestor in result.items():
    print(f"{leaf}: {max_ancestor}")


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []  # Multiple children

def find_max_ancestor_for_leaves(root):
    if not root:
        return {}

    leaf_max_ancestor = {}

    def dfs(node, max_ancestor):
        if not node:
            return

        # Update max ancestor for the current path
        max_ancestor = max(max_ancestor, node.val)

        # If it's a leaf node, store the max ancestor
        if not node.children:
            leaf_max_ancestor[node.val] = max_ancestor
            return

        # Recur for all children
        for child in node.children:
            dfs(child, max_ancestor)

    dfs(root, float('-inf'))  # Start DFS with smallest possible max
    return leaf_max_ancestor

# Constructing an example tree:
#         4
#      /  |  \
#     5   3   7
#    /   / \
#   1   2   6
root = TreeNode(4)
root.children.append(TreeNode(5))
root.children.append(TreeNode(3))
root.children.append(TreeNode(7))
root.children[0].children.append(TreeNode(1))
root.children[1].children.append(TreeNode(2))
root.children[1].children.append(TreeNode(6))

# Compute and print results
result = find_max_ancestor_for_leaves(root)
for leaf, max_ancestor in result.items():
    print(f"{leaf}: {max_ancestor}")

from collections import defaultdict

def find_max_ancestor_for_leaves_from_edges(edges):
    if not edges:
        return {}

    # Step 1: Build adjacency list and find root
    tree = defaultdict(list)
    incoming_edges = set()  # Used to find root

    for parent, child in edges:
        tree[parent].append(child)
        incoming_edges.add(child)

    # Find the root (the node that never appears as a child)
    root = None
    for parent, _ in edges:
        if parent not in incoming_edges:
            root = parent
            break

    if root is None:
        return {}  # No valid root found

    # Step 2: DFS to find max ancestor for leaf nodes
    leaf_max_ancestor = {}

    def dfs(node, max_ancestor):
        if node not in tree:  # Leaf node
            leaf_max_ancestor[node] = max_ancestor
            return

        max_ancestor = max(max_ancestor, node)
        for child in tree[node]:
            dfs(child, max_ancestor)

    dfs(root, float('-inf'))
    return leaf_max_ancestor

# Given edges
edges = [(4, 5), (4, 3), (5, 1), (3, 2), (3, 6)]

# Compute and print results
result = find_max_ancestor_for_leaves_from_edges(edges)
for leaf, max_ancestor in result.items():
    print(f"{leaf}: {max_ancestor}")
