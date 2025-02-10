# Same as leetcode 1031 but here the size is infinite
# https://leetcode.com/problems/escape-a-large-maze/solutions/282849/python-bfs-and-dfs-the-whole-problem-is-broken/

from collections import deque

def min_knight_moves(start, target, blocked):
    """
    Computes the minimum number of moves for a knight to get from start to target on an
    infinite chessboard with some blocked cells.

    Parameters:
      start   : tuple (x, y) starting coordinate.
      target  : tuple (x, y) target coordinate.
      blocked : list of [x, y] coordinates that are blocked.

    Returns:
      Minimum number of moves (an integer) to reach target, or -1 if unreachable.
    """
    # If start is target, no moves needed.
    if start == target:
        return 0

    # Create a set for O(1) lookups of blocked cells.
    blocked_set = { (x, y) for x, y in blocked }
    B = len(blocked)

    # If there are obstacles, determine the maximum area they can enclose.
    # (If B==0, we will not restrict by a tight bound.)
    threshold = (B * (B - 1)) // 2 if B > 0 else None

    # Choose a margin: if obstacles exist, use the threshold; otherwise, use a default.
    margin = threshold if threshold is not None and threshold > 0 else 50

    # Define a bounding box that surely contains start and target,
    # and is extended by "margin" on all sides.
    min_x = min(start[0], target[0]) - margin
    max_x = max(start[0], target[0]) + margin
    min_y = min(start[1], target[1]) - margin
    max_y = max(start[1], target[1]) + margin

    # All possible knight moves.
    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                    (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Set up the BFS.
    queue = deque()
    queue.append( (start[0], start[1], 0) )  # (x, y, moves)
    visited = set()
    visited.add( (start[0], start[1]) )

    while queue:
        x, y, moves = queue.popleft()

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy

            # Skip if the new cell is blocked.
            if (nx, ny) in blocked_set:
                continue

            # Enforce the bounding box limits.
            if nx < min_x or nx > max_x or ny < min_y or ny > max_y:
                continue

            if (nx, ny) in visited:
                continue

            # Found the target!
            if (nx, ny) == target:
                return moves + 1

            visited.add((nx, ny))
            queue.append((nx, ny, moves + 1))

    # If the BFS completes without reaching the target,
    # then the obstacles must be “trapping” the knight.
    return -1


# -------------------------------
# Example usage:
if __name__ == '__main__':
    # Define start, target, and blocked cells.
    start = (0, 0)
    target = (4, 5)
    blocked = [
        [1, 2], [2, 3], [3, 3], [2, 1]
    ]
    
    result = min_knight_moves(start, target, blocked)
    print("Minimum knight moves:", result)
