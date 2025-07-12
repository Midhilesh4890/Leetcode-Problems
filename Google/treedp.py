def solve_min_cut(root, edges):
    from collections import defaultdict
    
    # Build adjacency: { node: [(neighbor, cost), ...] }
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Memo to store dp(u) = cost to disconnect node u from its parent
    dp = {}

    def dfs(u, parent):
        # If dp already computed, return it
        if u in dp:
            return dp[u]
        
        # Find children (all neighbors except the parent)
        children = [(v, w) for v, w in graph[u] if v != parent]
        
        # If leaf, must cut edge to parent
        # (Cost is 0 if u is root and has no parent-edge. We'll handle root outside.)
        if len(children) == 0:
            # cost to cut edge from u->parent (lookup from adjacency)
            # We'll find w in adjacency from parent->u or u->parent
            # But if there's no parent, this is the root or single-node tree
            if parent is None:
                dp[u] = 0  # If single node is root, no cost
            else:
                # Find cost of edge from parent->u
                for nei, cost in graph[u]:
                    if nei == parent:
                        dp[u] = cost
                        break
            return dp[u]

        # If non-leaf:
        # costIfCut = cost to cut the edge to the parent
        costIfCut = 0
        if parent is not None:
            # find the edge cost from u->parent
            for nei, cost in graph[u]:
                if nei == parent:
                    costIfCut = cost
                    break
        
        # costIfNotCut = sum of dp(child) for all children
        costIfNotCut = 0
        for (c, w_c) in children:
            costIfNotCut += dfs(c, u)

        dp[u] = min(costIfCut, costIfNotCut) if parent is not None else costIfNotCut
        return dp[u]
    
    # The final answer is the sum of dp(child) for all children of root
    # because the root has no parent, so we don't directly pay for an edge to the root.
    ans = 0
    for (child, w_child) in graph[root]:
        ans += dfs(child, root)
    
    return ans

# ------------------------------
# Example usage:

# 1) First example
edges1 = [
    (6, 4, 5),
    (6, 2, 2),
    (4, 1, 1)
]
print(solve_min_cut(6, edges1))  # Expect 3

# 2) Second example
edges2 = [
    (6, 3, 4),
    (6, 5, 2),
    (3, 7, 3),
    (3, 8, 5),
    (5, 4, 1)
]
print(solve_min_cut(6, edges2))  # Expect 5

class Node:
    """
    Simple class to represent an N-ary tree node.
    - val:    The integer value/data for the node (if needed).
    - children: List of child nodes (also Node objects).
    - costs:  A list of edge costs, where costs[i] is the cost of
              the edge connecting this node to children[i].
    """
    def __init__(self, val):
        self.val = val
        self.children = []
        self.costs = []

def dfs(node, parent_edge_cost):
    """
    Perform a DFS-based DP to compute the minimal cost for 'node' to
    be disconnected from its parent. The 'parent_edge_cost' is the cost
    of the edge from 'node' to its parent.

    We return the minimal cost needed so that 'node' (and its entire subtree)
    does NOT remain connected to its parent node.
    
    The logic:
      1) If 'node' is a leaf (no children), we MUST cut the edge to the parent.
         Hence, cost = parent_edge_cost.
      2) Otherwise (node has children):
         - Option A: Cut parent->node edge (cost = parent_edge_cost).
         - Option B: Keep parent->node edge, but then we must cut all edges to
           node's children so the children are no longer connected to node.
           That cost = sum(dfs(child, edge_cost)) for all child edges.
         We take the minimum of those two options.
      3) If 'node' has no parent_edge_cost (i.e., node is root),
         we skip "cut to parent" and only consider cutting children.

    :param node: A Node in the N-ary tree
    :param parent_edge_cost: The cost of the edge from this node to its parent.
                             None or 0 if this node is the root.
    :return: Minimal cost to ensure 'node' is not connected to its parent.
    """
    # If node has no children, it's a leaf -> MUST cut edge to parent
    if not node.children:
        # If node is also the root (parent_edge_cost = None), cost is 0
        if parent_edge_cost is None:
            return 0
        return parent_edge_cost

    # For a non-leaf node, we have two choices:

    # 1) CUT edge to parent. If node is the root (parent_edge_cost is None),
    #    there's nothing to cut; costIfCut = 0 in that scenario.
    cost_if_cut = parent_edge_cost if parent_edge_cost is not None else 0

    # 2) DON'T CUT edge to parent. Then we must cut each child's edge to node.
    cost_if_not_cut = 0
    for i, child in enumerate(node.children):
        # 'node.costs[i]' is the cost of node->child edge
        edge_cost_to_child = node.costs[i]
        cost_if_not_cut += dfs(child, edge_cost_to_child)

    # If node isn't the root, we take min of cutting or not cutting the parent-edge.
    # If node is the root, only the "not cut" scenario is relevant (the cost of children).
    if parent_edge_cost is not None:
        return min(cost_if_cut, cost_if_not_cut)
    else:
        return cost_if_not_cut  # Root has no parent-edge to cut

def min_cut_for_root(root):
    """
    Computes the minimal cost to disconnect all leaves from the given root.
    
    Since the root itself doesn't have a parent edge, we effectively sum the
    costs needed to disconnect each of the root's children from it.
    """
    if root is None:
        return 0

    total_cost = 0
    # For each child of the root, we call dfs(child, edge_cost)
    for i, child in enumerate(root.children):
        edge_cost_to_child = root.costs[i]
        total_cost += dfs(child, edge_cost_to_child)

    return total_cost

# ----------------------------------------------------------------------
# DEMO: Example usage matching your second sample (but for an N-ary tree).
#
# Tree structure:
#     6 (root)
#    / \
#   3   5
#  / \   \
# 7   8   4
#
# Edge costs:
# (6-3) = 4
# (6-5) = 2
# (3-7) = 3
# (3-8) = 5
# (5-4) = 1
#
# Expected minimal cut cost = 5.

if __name__ == "__main__":
    # Create the root
    root = Node(6)

    # Create other nodes
    node3 = Node(3)
    node5 = Node(5)
    node7 = Node(7)
    node8 = Node(8)
    node4 = Node(4)

    # Build the tree (root has two children: 3 & 5)
    root.children = [node3, node5]
    # Corresponding costs from root->(3) is 4, and root->(5) is 2
    root.costs   = [4, 2]

    # node3 has two children: 7 & 8
    node3.children = [node7, node8]
    node3.costs    = [3, 5]

    # node5 has one child: 4
    node5.children = [node4]
    node5.costs    = [1]

    # Compute the minimal cut
    answer = min_cut_for_root(root)
    print("Minimal cut cost =", answer)  # Should print "Minimal cut cost = 5"
