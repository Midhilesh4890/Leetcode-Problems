# Initial Question: You are given an n×m grid and start from the bottom-left corner with the goal of reaching the bottom-right corner. The allowed moves are only to the right, diagonally up-right, and diagonally down-right. The task is to determine the total number of unique paths that can lead you from the starting point to the destination while adhering to these movement rules.


# Follow-Up 1: A list of specific checkpoints within the grid is now introduced. In this variation, you are required to count only those paths that pass through each of these checkpoints once before reaching the bottom-right corner.


# Follow-Up 2: The order of visiting these checkpoints is now specified. For example, if the checkpoints are labeled 1, 2, and 3, any valid path must encounter checkpoint 1 first, then checkpoint 2, and finally checkpoint 3, in that exact sequence, on its way to the destination.


from collections import defaultdict

def count_total_paths(n, m):
    """
    Count the total number of unique paths in an n x m grid from the bottom-left corner (0,0)
    to the bottom-right corner (0, m-1) using only the moves:
       - Right: (r, c) -> (r, c+1)
       - Diagonally up-right: (r, c) -> (r+1, c+1)
       - Diagonally down-right: (r, c) -> (r-1, c+1)
    
    The grid rows are 0-indexed with 0 as the bottom row and n-1 as the top row.
    """
    # Initialize a 2D list (n rows x m columns) with zeros.
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1  # start at (0,0)

    # Process each column (except the last, since moves go to the next column).
    for c in range(m - 1):
        for r in range(n):
            if dp[r][c] != 0:
                # Move right (same row)
                dp[r][c + 1] += dp[r][c]
                # Move diagonally up-right (if not at the top)
                if r + 1 < n:
                    dp[r + 1][c + 1] += dp[r][c]
                # Move diagonally down-right (if not at the bottom)
                if r - 1 >= 0:
                    dp[r - 1][c + 1] += dp[r][c]
    # Return the number of ways to get to the bottom-right corner (row 0, column m-1)
    return dp[0][m-1]

def count_paths_with_checkpoints(n, m, checkpoints):
    """
    Count the number of unique paths in an n x m grid from (0,0) to (0, m-1)
    that pass through all the specified checkpoints at least once (order does not matter).
    
    Parameters:
      n, m: grid dimensions.
      checkpoints: a list of tuples (r, c) representing checkpoint coordinates.
      
    We use a DP where the state is (row, column, mask) where mask (a bitmask) represents 
    which of the checkpoints have been visited so far.
    """
    # Map each checkpoint to a unique bit position.
    checkpoint_index = {}
    for i, (r, c) in enumerate(checkpoints):
        checkpoint_index[(r, c)] = i
    full_mask = (1 << len(checkpoints)) - 1  # all checkpoints visited when mask equals full_mask

    # Create a list of dictionaries for each column.
    # For column c, dp[c] is a dictionary mapping (row, mask) --> number of ways.
    dp = [defaultdict(int) for _ in range(m)]
    
    # Start at (0,0). If (0,0) is a checkpoint, mark it as visited.
    init_mask = 0
    if (0, 0) in checkpoint_index:
        init_mask |= (1 << checkpoint_index[(0, 0)])
    dp[0][(0, init_mask)] = 1

    # Process the grid column by column.
    for c in range(m - 1):
        for (r, mask), ways in dp[c].items():
            # Try all three allowed moves.
            for dr in [0, 1, -1]:
                nr = r + dr
                nc = c + 1
                if 0 <= nr < n:
                    new_mask = mask
                    # If the new cell is a checkpoint, mark it as visited.
                    if (nr, nc) in checkpoint_index:
                        new_mask |= (1 << checkpoint_index[(nr, nc)])
                    dp[nc][(nr, new_mask)] += ways

    # We only want to count paths that end at (0, m-1) with all checkpoints visited.
    return dp[m-1].get((0, full_mask), 0)

def count_segment_paths(n, start, end):
    """
    Count the number of paths from 'start' to 'end' in an n x m grid (only considering
    the columns between start and end) using the allowed moves.
    
    Both 'start' and 'end' are tuples (r, c). We assume that end[1] >= start[1].
    """
    (r_start, c_start) = start
    (r_end, c_end) = end
    if c_end < c_start:
        # Cannot move left.
        return 0
    # The number of columns in this segment (inclusive of start and end columns).
    width = c_end - c_start + 1
    # dp[i][r] will be the number of ways to reach row r at the i-th column of the segment.
    dp = [[0 for _ in range(n)] for _ in range(width)]
    dp[0][r_start] = 1

    # Process each column in the segment.
    for i in range(width - 1):
        for r in range(n):
            if dp[i][r]:
                for dr in [0, 1, -1]:
                    nr = r + dr
                    if 0 <= nr < n:
                        dp[i+1][nr] += dp[i][r]
    # The answer for this segment is the number of ways to get to row r_end at the last column.
    return dp[width - 1][r_end]

def count_paths_ordered_checkpoints(n, m, checkpoints_ordered):
    """
    Count the number of unique paths in an n x m grid from (0,0) to (0, m-1) that
    pass through the checkpoints in the given order.
    
    Parameters:
      n, m: grid dimensions.
      checkpoints_ordered: a list of tuples (r, c) that must be visited in the specified order.
      
    We break the problem into segments:
      - from the start (0,0) to the first checkpoint,
      - from the first checkpoint to the second, etc.,
      - and finally from the last checkpoint to the destination (0, m-1).
    The total number of valid paths is the product of the number of ways for each segment.
    """
    # Create the full ordered list of required points.
    points = [(0, 0)] + checkpoints_ordered + [(0, m-1)]
    total_paths = 1
    # Compute the number of paths for each segment.
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i+1]
        # It must be that the column index of 'end' is not before that of 'start'.
        if end[1] < start[1]:
            return 0
        segment_paths = count_segment_paths(n, start, end)
        total_paths *= segment_paths
        # If any segment has no valid paths, the entire product is zero.
        if total_paths == 0:
            return 0
    return total_paths

# --- Example usage: ---

if __name__ == '__main__':
    # Set grid dimensions.
    n = 5  # number of rows (0 is bottom, 4 is top)
    m = 5  # number of columns (0 is left, 4 is right)

    # === Initial Question: No checkpoints ===
    total = count_total_paths(n, m)
    print("Total paths (no checkpoints):", total)

    # === Follow-Up 1: Checkpoints (order does not matter) ===
    # For example, require that the path passes through (1,2) and (3,3).
    checkpoints = [(1, 2), (3, 3)]
    total_with_checkpoints = count_paths_with_checkpoints(n, m, checkpoints)
    print("Paths with checkpoints (any order):", total_with_checkpoints)

    # === Follow-Up 2: Ordered checkpoints ===
    # For example, require that the path visits (1,2) first then (3,3).
    checkpoints_ordered = [(1, 2), (3, 3)]
    total_ordered = count_paths_ordered_checkpoints(n, m, checkpoints_ordered)
    print("Paths with ordered checkpoints:", total_ordered)
