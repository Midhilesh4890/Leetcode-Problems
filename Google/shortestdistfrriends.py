# Round 1:
# Question: There are n friends living in different cities across a graph. Find the shortest distance between two friends (e.g., A and B).
# Solution: Solved using BFS (Dijkstra's algorithm).
# Follow-up: Given k friends, find the node where the total distance for all friends to reach is minimized.
# Solution: Solved by applying BFS from each friend and checking nodes that all k friends visit.


import heapq  # Importing heapq to use a priority queue for efficient shortest path computation

def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.

    Parameters:
        graph (dict): A dictionary where each key is a node, and its value is a list of tuples (neighbor, weight).
        start (str): The starting node for the algorithm.

    Returns:
        dict: A dictionary where keys are nodes and values are the shortest distances from the start node.
    """

    # Initialize distances to all nodes as infinity, except the start node which has distance 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min-heap priority queue to keep track of the nodes with the shortest known distance
    queue = [(0, start)]  # (distance, node)

    while queue:
        # Extract the node with the smallest known distance
        d, node = heapq.heappop(queue)

        # If the extracted distance is greater than the known shortest distance, skip processing
        if d > distances[node]:
            continue

        # Explore each neighboring node
        for neighbor, weight in graph[node]:
            nd = d + weight  # Calculate the new possible shortest distance

            # If the new distance is smaller than the currently known shortest distance, update it
            if nd < distances[neighbor]:
                distances[neighbor] = nd
                heapq.heappush(queue, (nd, neighbor))  # Push the updated distance into the priority queue

    return distances  # Return the dictionary of shortest distances from the start node

# Define the graph as an adjacency list where keys are nodes and values are lists of (neighbor, weight) pairs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Define the two friends' locations
friendA = 'A'  # Starting point
friendB = 'D'  # Destination point

# Run Dijkstra's algorithm from friendA's location
distances = dijkstra(graph, friendA)

# Output the shortest distance between friendA and friendB
print("Shortest distance between {} and {}: {}".format(friendA, friendB, distances[friendB]))


import heapq

def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from a start node to all other nodes in a weighted graph.

    Parameters:
    - graph (dict): A dictionary where keys are node names and values are lists of tuples (neighbor, weight).
    - start (str): The starting node for the shortest path computation.

    Returns:
    - distances (dict): A dictionary mapping each node to its shortest distance from the start node.
    """
    # Initialize all distances to infinity except for the start node (set to 0)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue (min-heap) to process nodes in order of their shortest known distance
    queue = [(0, start)]

    while queue:
        # Extract the node with the smallest known distance
        d, node = heapq.heappop(queue)

        # If the extracted distance is greater than the currently known distance, skip processing
        if d > distances[node]:
            continue

        # Relax the edges by checking neighbors
        for neighbor, weight in graph[node]:
            new_distance = d + weight

            # If a shorter path is found, update and push the new distance into the priority queue
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances  # Return shortest distances from the start node to all nodes

# Graph representation using adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],  # Node A connects to B (weight 1) and C (weight 4)
    'B': [('A', 1), ('C', 2), ('D', 5)],  # Node B connects to A, C, and D
    'C': [('A', 4), ('B', 2), ('D', 1)],  # Node C connects to A, B, and D
    'D': [('B', 5), ('C', 1)]  # Node D connects to B and C
}

# List of friend locations in the graph
friend_nodes = ['A', 'B', 'D']

# Dictionary to store the total shortest distance from all friends to each node
total_dist = {node: 0 for node in graph}

# Compute the total distance of all nodes from each friend's location
for friend in friend_nodes:
    distances = dijkstra(graph, friend)  # Compute shortest paths from the friend's location
    for node in graph:
        total_dist[node] += distances[node]  # Sum up the shortest distances to each node

# Find the node with the minimum total distance from all friends
best_node = min(total_dist, key=total_dist.get)

# Print the optimal meeting node and its total distance from all friends
print("Best meeting node:", best_node, "with total distance:", total_dist[best_node])
