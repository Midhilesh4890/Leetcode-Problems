
# Question is about a frog which can go left or right with with maximum possible 
# step be l for left and r for right, 
# i.e. frog can move right 0 or 1, or 2 or ... r times, 
# given start and destination, find minimum steps to reach.

from collections import deque

def min_steps_to_reach(start, destination, l, r):
    if start == destination:
        return 0  # Already at the destination

    queue = deque([(start, 0)])  # (position, steps)
    visited = set([start])       # To avoid revisiting

    while queue:
        pos, steps = queue.popleft()

        # Try all possible moves
        for move in range(-l, r + 1):  # Moving from -l to r
            new_pos = pos + move
            if new_pos == destination:
                return steps + 1  # Found the shortest path
            
            if new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, steps + 1))
    
    return -1  # If destination is unreachable

# Example usage:
start = 0
destination = 5
l = 2
r = 3
print(min_steps_to_reach(start, destination, l, r))  # Output: Minimum steps to reach
