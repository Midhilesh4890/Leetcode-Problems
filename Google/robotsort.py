# Robot sort:
# You have boxes in magazine and a single empty spot (at the end) like:


# 1, 4, 2, 5, 3, _


# You have a robot which needs to sort boxes. It can only pick up single box, put it in empty box and then pick another one up. Sort boxes to have either _, 1, 2, 3, 4, 5 or 1, 2, 3, 4, 5, _
# What is the fastest way to sort if robot knows immediately where are boxes with specific numbers, but it takes time for him to move.


# I provided 2 solutions: selection sort, to always put correct element in empty spot since we know where everything is, but it still is O(n^2) and seems to unnecessarily jump over other elements, which doesn't seem optimal or some version of insertion / bubble sort, although it was difficult with only 1 empty spot, to shift elements. I don't know what is correct solution.

def compute_min_moves(boxes, empty_target_index):
    # Get the total number of positions (boxes plus one empty)
    n = len(boxes)
    
    # Create the target (sorted) configuration based on where the empty should be.
    # If the empty is to be at the beginning (index 0):
    #   target configuration is [None] followed by the sorted boxes.
    # If the empty is to be at the end (index n-1):
    #   target configuration is the sorted boxes followed by [None].
    sorted_boxes = sorted(x for x in boxes if x is not None)
    if empty_target_index == 0:
        target = [None] + sorted_boxes
    elif empty_target_index == n - 1:
        target = sorted_boxes + [None]
    else:
        raise ValueError("empty_target_index must be either 0 or n-1")
    
    # Build a mapping from each current index to its target index.
    # For a box (a number), find its position in the target configuration.
    # For the empty spot (None), always map it to the target empty index.
    mapping = [None] * n
    for i in range(n):
        if boxes[i] is None:
            mapping[i] = empty_target_index
        else:
            mapping[i] = target.index(boxes[i])
    
    # We'll decompose the permutation into cycles.
    # Create a visited list to keep track of indices that are already in a cycle.
    visited = [False] * n
    moves = 0
    # Record the index where the empty slot is initially located.
    initial_empty_index = boxes.index(None)
    
    # Loop over every index to identify cycles.
    for i in range(n):
        if visited[i]:
            continue  # Skip indices already included in a cycle.
        cycle = []
        cur = i
        # Follow the mapping until a cycle is closed.
        while not visited[cur]:
            visited[cur] = True
            cycle.append(cur)
            cur = mapping[cur]
        # If the cycle has only one element, no move is needed.
        if len(cycle) == 1:
            continue
        # For each cycle, determine its cost:
        # - If the cycle contains the initial empty slot, we can fix it in (cycle length - 1) moves.
        # - If it does not, we need one extra move to incorporate the empty into the cycle,
        #   for a total cost of (cycle length + 1) moves.
        if initial_empty_index in cycle:
            moves += len(cycle) - 1
        else:
            moves += len(cycle) + 1
    return moves

def min_robot_sort_steps(boxes):
    # We have two valid final configurations:
    # Option 1: Empty at the beginning (index 0)
    # Option 2: Empty at the end (index len(boxes)-1)
    # Compute the moves required for both options.
    moves_empty_first = compute_min_moves(boxes, 0)
    moves_empty_last = compute_min_moves(boxes, len(boxes) - 1)
    # Return the minimum moves required of the two possibilities.
    return min(moves_empty_first, moves_empty_last)

# Example usage:
if __name__ == '__main__':
    # Initial configuration: boxes with numbers and a single empty spot represented by None.
    # For example, [1, 4, 2, 5, 3, None] means positions 0 to 4 hold boxes 1, 4, 2, 5, 3,
    # and position 5 is empty.
    configuration = [1, 4, 2, 5, 3, None]
    
    # Compute the minimal number of moves needed for the robot to sort the boxes.
    minimal_moves = min_robot_sort_steps(configuration)
    
    # Print out the minimum moves required.
    print("Minimum moves required:", minimal_moves)
