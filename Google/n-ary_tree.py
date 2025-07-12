class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def __repr__(self):
        return f"{self.value}"


def remove_leaves(root):
    # Build a mapping from child node to its parent.
    parent = {}   # Maps a node to its parent.
    leaves = []   # List of nodes that are leaves.
    
    # Use a queue for a BFS traversal to build parent pointers.
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node.children:
            leaves.append(node)
        else:
            for child in node.children:
                parent[child] = node
                queue.append(child)
    
    result = []
    
    # Iteratively remove leaves and update parent pointers.
    while leaves:
        new_leaves = []
        for leaf in leaves:
            result.append(leaf.value)
            if leaf in parent:
                par = parent[leaf]
                # Remove the leaf from its parent's children list.
                par.children.remove(leaf)
                # If the parent becomes a leaf, add it to the next round.
                if not par.children:
                    new_leaves.append(par)
        leaves = new_leaves
        
    return result


# Build the test tree:
#         1
#      /  |  \
#     2   5   3
#    / \   |
#   7   4  9
#       |
#       8

# Create nodes.
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

# Construct the tree structure.
n1.children = [n2, n5, n3]
n2.children = [n7, n4]
n5.children = [n9]
n4.children = [n8]

# Expected removal order: [7, 8, 9, 3, 4, 5, 2, 1]
output = remove_leaves(n1)
print("Output:", output)
print("Expected Output:", [7, 8, 9, 3, 4, 5, 2, 1])
