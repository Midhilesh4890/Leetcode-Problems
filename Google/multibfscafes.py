from collections import deque, defaultdict

def find_best_cafe(adj_list, friends, cafes):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v in adj_list:
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: Multi-source BFS from all friends
    queue = deque()
    distances = {}  # {node: shortest distance from any friend}
    
    for friend in friends:
        queue.append((friend, 0))  # (current location, distance)
        distances[friend] = 0  # Distance from itself is 0

    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in distances:  # If not visited
                distances[neighbor] = dist + 1  # Update shortest distance
                queue.append((neighbor, dist + 1))  # Add neighbor to queue

    # Step 3: Find the café that minimizes the maximum distance from all friends
    min_max_distance = float('inf')
    best_cafe = None
    
    for cafe in cafes:
        if cafe not in distances:  # If a café is unreachable by any friend, skip it
            continue
        max_dist = max(distances[friend] for friend in friends)  # Distance of each friend to the café
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_cafe = cafe

    return best_cafe

# Example Usage:
adj_list = [(1, 2), (2, 3), (3, 4), (4, 5), (3, 6), (6, 7), (7, 8)]
friends = [1, 5]
cafes = [4, 7]

print(find_best_cafe(adj_list, friends, cafes))  # Expected Output: 4
