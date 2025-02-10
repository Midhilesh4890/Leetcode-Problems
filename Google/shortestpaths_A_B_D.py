# Given an undirected graph, Alice and Bob are standing somewhere (node index is given), They want to reach a common destination D such that the number of unique edges they traverse is as minimum as possible. (Most hops should be common.!)
# Another way of writing this question 
# Q: A and B wants to reach some destination in an undirected graph using the least number of unique edges.
# Find the count of unique edges.


# Let's say the two paths come out to be this..
# A-x-y-D
# B-y-D


# Output : 4


# Explanation :
# A-x, x-y, y-D and B-y

from collections import deque

def bfs(graph, vertex):
    """
    Perform a breadth-first search on the graph from the vertex node.
    Returns a dictionary of distances from 'vertex' to every reachable node.
    """
    distances = {vertex: 0}
    queue = deque([vertex])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances

def minimum_unique_edges(graph, A, B, D):
    """
    Computes the vertex v that minimizes:
       d(A, v) + d(B, v) + d(v, D)
    where d(X, Y) is the shortest-path distance between X and Y.
    
    Returns a tuple (best_v, min_edges) where best_v is the meeting point and
    min_edges is the minimum number of unique edges traversed.
    """
    # Compute shortest path distances from A, B, and D
    dist_from_A = bfs(graph, A)
    dist_from_B = bfs(graph, B)
    dist_from_D = bfs(graph, D)
    print(dist_from_A)
    print(dist_from_B)
    print(dist_from_D)
    min_edges = float('inf')
    best_v = None
    
    # Iterate over all vertices in the graph
    for v in graph:
        # Only consider v if it is reachable from A, B, and D
        if v in dist_from_A and v in dist_from_B and v in dist_from_D:
            candidate = dist_from_A[v] + dist_from_B[v] + dist_from_D[v]
            if candidate < min_edges:
                min_edges = candidate
                best_v = v
                
    return best_v, min_edges

if __name__ == "__main__":
    # Example graph:
    # Vertices: 0, 1, 2, 3
    # Edges: 0-2, 1-2, 0-3, 1-3, 2-3
    graph = {
        0: [2, 3],
        1: [2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }
    
    # Starting positions for Alice and Bob, and the destination D
    A = 0  # Alice's starting node
    B = 1  # Bob's starting node
    D = 3  # Destination node
    
    best_v, min_edges = minimum_unique_edges(graph, A, B, D)
    
    if best_v is not None:
        print("Best meeting point (v):", best_v)
        print("Minimum number of unique edges traversed:", min_edges)
    else:
        print("No meeting point found such that all nodes are reachable from A, B, and D.")

###########################################################################################

from collections import deque

def bfs(graph, start):
    """
    Performs a breadth-first search on the graph from the start node.
    Returns a dictionary mapping each reachable node to its distance from start.
    """
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances

def multi_source_sum_distances(graph, sources):
    """
    For each vertex in the graph, computes the sum of distances from all sources.
    Also returns a dictionary telling how many sources reached each vertex.
    """
    # Initialize dictionaries for summing distances and counting sources
    sum_distances = {v: 0 for v in graph}
    count_reached = {v: 0 for v in graph}
    
    # Run a BFS for each source and accumulate the distances
    for s in sources:
        dist = bfs(graph, s)
        for v, d in dist.items():
            sum_distances[v] += d
            count_reached[v] += 1
    return sum_distances, count_reached

def minimum_unique_edges_multi_source(graph, sources, D):
    dist_from_D = bfs(graph, D)
    
    # Compute the sum of distances from all sources and the count of sources reaching each vertex
    sum_distances, count_reached = multi_source_sum_distances(graph, sources)
    
    min_edges = float('inf')
    best_v = None
    
    # Consider every vertex in the graph as a candidate meeting point
    for v in graph:
        # Check that v is reachable from all sources and from D
        if count_reached[v] == len(sources) and v in dist_from_D:
            candidate = sum_distances[v] + dist_from_D[v]
            if candidate < min_edges:
                min_edges = candidate
                best_v = v
                
    return best_v, min_edges

if __name__ == "__main__":
    # Example graph (undirected):
    # Let's create a graph where the vertices and their connections are as follows:
    #
    #   0 -- 2 -- 3 -- 4
    #    \  /     |
    #     1       |
    #      \------/
    #
    # The adjacency list representation:
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]
    }
    
    # Let our K sources be 0, 1, and 2
    sources = [0, 1, 2]
    
    # And let the destination be 4
    D = 4
    
    best_v, min_edges = minimum_unique_edges_multi_source(graph, sources, D)
    
    if best_v is not None:
        print("Best meeting point (v):", best_v)
        print("Minimum number of unique edges traversed:", min_edges)
    else:
        print("No meeting point found that is reachable from all sources and D.")
