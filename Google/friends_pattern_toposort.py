# You and your friends discuss a pattern of number your teacher has written on blackboard after class. 
# 
#Return false if there is any contradiction between you and your friends, in sequencing of numbers, else return true.


# For e.g Suppose 4 friends write a sequence of numbers
# Friend 1: 1, 3, 4, 2
# Friend 2: 3, 4, 9, 10
# Friend 3: 11, 49, 13, 3
# Friend 4: 19, 3, 13, 4


# Ans. False, there is contradiction

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

    # Topological Sorting (Kahn's Algorithm) - Detect Cycle
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
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
