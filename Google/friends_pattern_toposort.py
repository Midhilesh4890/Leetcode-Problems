from collections import defaultdict, deque

def has_contradiction(sequences):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # Build the graph
    for seq in sequences:
        for i in range(len(seq) - 1):
            if seq[i+1] not in graph[seq[i]]:  # Avoid duplicate edges
                graph[seq[i]].add(seq[i+1])
                in_degree[seq[i+1]] += 1
            if seq[i] not in in_degree:
                in_degree[seq[i]] = 0  # Initialize nodes
    print(graph)
    print(in_degree)
    # Topological Sorting (Kahn's Algorithm) - Detect Cycle
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    print(queue)
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    print(len(sorted_order))
    print(len(in_degree))
    # If the sorted order doesn't include all nodes, there is a cycle
    return len(sorted_order) == len(in_degree)

# Example Test Case
sequences = [
    [1, 3, 4, 2],
    [3, 4, 9, 10],
    [11, 49, 13, 3],
    [19, 3, 13, 4]
]

print(has_contradiction(sequences))  # Output: False (contradiction exists)
