# Question:
# You are given a matrix of 0s, 1s, and 2s, where 0 means an empty cell, 1 means a wall, and 2 means an exit. There will always be an exit. Generate a sequence of instructions (U, D, L, R) such that no matter where you start in the matrix, you always reach the exit.
# Example:


# 1 0 1  
# 0 2 0  
# 1 0 1  
# Answer: UDLR (No matter where you start, you’ll end up at 2).

from collections import deque

def find_sync_sequence(grid):
    """
    Given a grid (list of lists) where:
      - 0: empty cell
      - 1: wall (cannot be entered)
      - 2: exit (absorbing state)
    Returns a sequence (string of moves U, D, L, R) such that regardless of
    where you start in a non-wall cell, following the moves will guarantee
    that you eventually reach an exit.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Moves and their corresponding row, col offsets.
    moves = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    
    def next_position(pos, move):
        """
        Given a current position (i, j) and a move (U, D, L, R),
        returns the next position.
        
        Note:
         - If the current cell is an exit, it is absorbing (stay there).
         - If the move would leave the grid or hit a wall (grid cell 1), stay in place.
        """
        i, j = pos
        # If already at an exit, remain there.
        if grid[i][j] == 2:
            return pos
        
        di, dj = moves[move]
        new_i, new_j = i + di, j + dj
        
        # Check if out-of-bounds or a wall.
        if not (0 <= new_i < rows and 0 <= new_j < cols):
            return pos
        if grid[new_i][new_j] == 1:
            return pos
        return (new_i, new_j)
    
    # Our state is the set of all positions you could be in (starting from any non-wall cell)
    initial_states = {(i, j) for i in range(rows) for j in range(cols) if grid[i][j] != 1}
    
    # We'll use BFS over subsets of positions, storing each state as a frozenset.
    queue = deque()
    visited = set()
    
    init_state = frozenset(initial_states)
    queue.append((init_state, ""))  # (current set of positions, sequence so far)
    visited.add(init_state)
    
    while queue:
        state, seq = queue.popleft()
        
        # If all positions in the current state are exits, we are done.
        if all(grid[i][j] == 2 for i, j in state):
            return seq
        
        # Try each possible move.
        for move in moves:
            new_state = frozenset(next_position(pos, move) for pos in state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, seq + move))
    
    # In case no synchronizing sequence is found (should not happen if there is at least one exit).
    return None


if __name__ == '__main__':
    # Test Case 1: Provided Example
    # Grid:
    #   1 0 1
    #   0 2 0
    #   1 0 1
    grid1 = [
        [1, 0, 1],
        [0, 2, 0],
        [1, 0, 1]
    ]
    
    sequence1 = find_sync_sequence(grid1)
    if sequence1 is not None:
        print("Synchronizing sequence for grid1:", sequence1)
    else:
        print("No synchronizing sequence exists for grid1.")
    
    # Test Case 2: A Bigger Grid
    # Grid visualization (each number corresponds to):
    #   1: wall, 0: empty, 2: exit
    #
    #   1  0  0  0  1  0  2
    #   0  1  1  0  0  0  1
    #   0  0  2  0  1  0  0
    #   1  0  0  0  0  1  0
    #   0  2  1  0  0  0  0
    grid2 = [
        [1, 0, 0, 0, 1, 0, 2],
        [0, 1, 1, 0, 0, 0, 1],
        [0, 0, 2, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0],
        [0, 2, 1, 0, 0, 0, 0]
    ]
    
    sequence2 = find_sync_sequence(grid2)
    if sequence2 is not None:
        print("Synchronizing sequence for grid2:", sequence2)
    else:
        print("No synchronizing sequence exists for grid2.")
