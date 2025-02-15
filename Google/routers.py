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

routers = {
    "A": (0, 0),
    "B": (3, 4),
    "C": (6, 8),
    "D": (10, 10)
}
max_range = 5
print(can_reach_router("A", "C", max_range, routers))  # True
print(can_reach_router("A", "D", max_range, routers))  # False
