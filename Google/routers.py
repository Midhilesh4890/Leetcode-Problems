# given the name of source and destination router, max rannge of all routers and a map of router name and coordinates, return boolean indicatin wheter a signal sent from source can reach destination.
from collections import deque
from typing import Dict, Tuple
import math

def can_reach_router(source: str, destination: str, max_range: float, routers: Dict[str, Tuple[float, float]]) -> bool:
    if source not in routers or destination not in routers:
        return False  # If source or destination is missing, return False
    
    # Helper function to check if two routers are within range
    def in_range(router1, router2):
        x1, y1 = routers[router1]
        x2, y2 = routers[router2]
        return math.dist((x1, y1), (x2, y2)) <= max_range

    # BFS setup
    queue = deque([source])
    visited = set([source])
    
    while queue:
        current_router = queue.popleft()
        if current_router == destination:
            return True  # Destination reached
        
        # Check all other routers to see if they are within range
        for neighbor in routers:
            if neighbor not in visited and in_range(current_router, neighbor):
                queue.append(neighbor)
                visited.add(neighbor)
    
    return False  # If we exhaust BFS and never reach the destination

routers1 = {
    "A": (0, 0),
    "B": (3, 4),
    "C": (6, 8),
    "D": (10, 10)
}
max_range1 = 6  # Each router can reach the next one, but not ones after that

print(can_reach_router("A", "B", max_range1, routers1))  # True (direct connection)
print(can_reach_router("A", "C", max_range1, routers1))  # True (via B)
print(can_reach_router("A", "D", max_range1, routers1))  # True (A->B->C->D)

# Test Case 2: Disconnected components
routers2 = {
    "A": (0, 0),
    "B": (2, 2),
    "C": (20, 20),
    "D": (22, 22)
}
max_range2 = 5  # A and B can connect, C and D can connect, but no path from A/B to C/D

print(can_reach_router("A", "B", max_range2, routers2))  # True
print(can_reach_router("C", "D", max_range2, routers2))  # True
print(can_reach_router("A", "D", max_range2, routers2))  # False (no path)

# Test Case 3: Dense network
routers3 = {
    "A": (0, 0),
    "B": (4, 0),
    "C": (8, 0),
    "D": (0, 4),
    "E": (4, 4),
    "F": (8, 4),
    "G": (0, 8),
    "H": (4, 8),
    "I": (8, 8)
}
max_range3 = 4.1  # Each router can reach adjacent routers

print(can_reach_router("A", "I", max_range3, routers3))  # True (diagonal path exists)
print(can_reach_router("A", "C", max_range3, routers3))  # True (via B)