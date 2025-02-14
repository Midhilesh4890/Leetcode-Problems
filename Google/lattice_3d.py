# https://chatgpt.com/share/67afb042-66d8-800d-823a-c91becb81e5d

# given a lattice kinda graph where each node is either a torch node that has power 16 or wire node where value is 0,
# if power node is connected to wire node, it will transmit power to wire and value would become 15 from 0 (1 value would be lost during transmission), again if this wire node is connected to another wire node then value would become 14 of that node
# for eg 16 -> 0 -> 0 would become 15 -> 14 -> 13, unless there is one more torch node ahead, then
# 16 -> 0 -> 0 -> 16
# 16 -> 15 -> 14 -> 16
# 16 -> 15 -> 15 <- 16


# nothing was given, I had to tell how the representation would look like, in the end we need to return graph when the power had transmitted from all torch nodes to expected wire nodes. And graph in kinda lattice, like a cube (3 d).


# I represented graph using unordered_map<node, vector>
# where node is (block, data){
# this.block = block
# this.data = data
# }
# sample graph:

from collections import deque

def simulate_power_transmission(nodes, edges):
    """
    Simulates power transmission in a network of nodes connected by edges.
    
    Parameters:
    - nodes: List of integers representing the initial power values at each node.
             Torch nodes have an initial value of 16, while wire nodes start with 0.
    - edges: List of tuples, where each tuple (u, v) represents an undirected edge between nodes u and v.
    """
    n = len(nodes)  # Number of nodes
    graph = [[] for _ in range(n)]  # Adjacency list representation of the graph
    
    # Build the graph with undirected edges
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize the queue with torch nodes
    queue = deque()  # Double-ended queue for BFS
    for i in range(n):
        if nodes[i] == 16:  # If the node is a torch node (starting power of 16)
            queue.append((i, 16))  # Add the torch node to the queue with its power level

    # Process nodes using BFS
    while queue:
        current, power = queue.popleft()  # Get the next node and its current power level
        
        # Iterate over all neighbors of the current node
        for neighbor in graph[current]:
            new_power = power - 1  # Reduce power by 1 for transmission
            # If the transmitted power is greater than the current power at the neighbor
            if new_power > nodes[neighbor]:
                nodes[neighbor] = new_power  # Update the neighbor's power level
                queue.append((neighbor, new_power))  # Add the neighbor to the queue for further propagation

# Initial node values (power): torch nodes with 16, wire nodes with 0
nodes = [16, 0, 0, 16, 0]  # Node 0 and 3 are torch nodes; 1, 2, and 4 are wire nodes

# Edges between nodes: (from_node, to_node)
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]

# Simulate power transmission
simulate_power_transmission(nodes, edges)

# Output final values
for i, value in enumerate(nodes):
    print(f"Node {i}: Value = {value}")
