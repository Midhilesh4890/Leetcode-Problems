from collections import deque, defaultdict
import math

def bfs(graph, start):
    """
    Perform BFS on an unweighted graph starting at 'start'
    and return a dictionary mapping each reachable node to its distance.
    """
    distances = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances

def find_best_cafe(adj_list, friends, cafes):
    """
    Given an edge list 'adj_list' for an undirected unweighted graph,
    a list of friend locations, and a list of cafes,
    return the cafe that minimizes the maximum distance any friend must travel.
    
    This function uses BFS (instead of Dijkstra) because the graph is unweighted.
    """
    # Build the undirected graph.
    graph = defaultdict(list)
    for u, v in adj_list:
        graph[u].append(v)
        graph[v].append(u)
    
    # Compute shortest distances from each friend to all other nodes.
    friend_distances = {}
    for friend in friends:
        friend_distances[friend] = bfs(graph, friend)
    
    # For each café, compute the worst-case (maximum) distance from any friend.
    best_cafe = None
    best_max_distance = math.inf
    for cafe in cafes:
        max_distance = 0
        reachable = True
        for friend in friends:
            # If this cafe is unreachable for any friend, skip it.
            if cafe not in friend_distances[friend]:
                reachable = False
                break
            max_distance = max(max_distance, friend_distances[friend][cafe])
        if reachable and max_distance < best_max_distance:
            best_max_distance = max_distance
            best_cafe = cafe
    
    return best_cafe

# Example Usage:
adj_list = [(1, 2), (2, 3), (3, 4), (4, 5), (3, 6), (6, 7), (7, 8)]
friends = [1, 5]
cafes = [4, 7]

print(find_best_cafe(adj_list, friends, cafes))  # Expected output: 4
