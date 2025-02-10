from collections import deque
import math

def compute_dp_with_bfs(root, children, edge_cost):
    # Step 1: BFS to compute depths.
    depth = {}
    queue = deque([(root, 0)])
    while queue:
        node, d = queue.popleft()
        depth[node] = d
        for child in children.get(node, []):
            queue.append((child, d + 1))
    
    # Step 2: Get nodes in descending order of depth.
    nodes_sorted = sorted(depth.keys(), key=lambda x: depth[x], reverse=True)
    
    dp = {}
    INF = math.inf
    
    # Step 3: Process nodes from leaves upward.
    for node in nodes_sorted:
        # If node has no children, treat it as a leaf.
        if node not in children or not children[node]:
            dp[node] = INF  # Leaf node (if not the root) should force a cut at its parent's edge.
        else:
            total_cost = 0
            for child in children[node]:
                # cost of edge from node to child
                cost = edge_cost[(node, child)]
                total_cost += min(cost, dp[child])
            dp[node] = total_cost
    
    return dp[root]

# Example usage:
# Suppose our tree is represented as follows:
#       6
#      / \
#     4   2
#    /
#   1
#
# children = {6: [4, 2], 4: [1], 2: [], 1: []}
# edge_cost = {(6, 4): 5, (6, 2): 1, (4, 1): 10}
#
# For node 2 and 1, we treat them as leaves (dp = INF).

children = {
    6: [4, 2],
    4: [1],
    2: [],
    1: []
}
edge_cost = {
    (6, 4): 5,
    (6, 2): 1,
    (4, 1): 10
}

result = compute_dp_with_bfs(6, children, edge_cost)
print("Minimum cost:", result)  # Expected output: 6
