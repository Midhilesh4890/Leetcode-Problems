from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_islands_bfs(root):
    if not root:
        return 0

    visited = set()
    queue = deque()
    island_count = 0

    def bfs(node):
        queue.append(node)
        visited.add(node)
        while queue:
            curr = queue.popleft()
            for neighbor in [curr.left, curr.right]:
                if neighbor and neighbor.val == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for node in level_order_traversal(root):
        if node.val == 1 and node not in visited:
            island_count += 1
            bfs(node)  # Start BFS for this new island

    return island_count

def level_order_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    nodes = []
    while queue:
        node = queue.popleft()
        if node:
            nodes.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return nodes




def count_unique_island_sizes_bfs(root):
    if not root:
        return {}

    visited = set()
    queue = deque()
    unique_sizes = {}

    def bfs(node):
        queue.append(node)
        visited.add(node)
        size = 0  # Track island size
        while queue:
            curr = queue.popleft()
            size += 1  # Count this node in the island
            for neighbor in [curr.left, curr.right]:
                if neighbor and neighbor.val == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return size

    for node in level_order_traversal(root):
        if node.val == 1 and node not in visited:
            island_size = bfs(node)
            unique_sizes[island_size] = unique_sizes.get(island_size, 0) + 1

    return unique_sizes
