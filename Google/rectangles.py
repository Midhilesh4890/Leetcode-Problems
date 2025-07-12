# Three players, A, B, and C play an online game. 
# The game consists of a map in the shape of an RxC grid.
# Each player has to capture one or more cells in the RxC grid. 
# So, after the game, each cell would have the name of the player who captured it.

# The winner of the game will be the player who covers the largest rectangle area in the RxC grid. 
# Find the area of that largest rectangle.
  
# Example:

# +---+---+---+---+
# | B | A | A | C |
# +---+---+---+---+
# | B | A | A | B |
# +---+---+---+---+
# | C | C | A | A |
# +---+---+---+---+
# | B | B | C | C |
# +---+---+---+---+
  
# In the above 4x4 grid, the size of the largest rectangle is 4 and the corresponding winner would be A.
  
  
#   size? = 1000x1000 
#   cellsFilled? = true
#   there can be more players.
#   no.of players as List<String>
#   no more than 50 players
  
#   String board[][];
#   List<String> player;
  
# p = no. of players
# rxc = rows and column

# O(p x (rxc + (r * r)))
#  O(p * r*c)

# +---+---+---+---+
# | 0 | 1 | 1 | C |
# +---+---+---+---+
# | 0 | 1 | 1 | B |
# +---+---+---+---+
# | 0 | 0 | 1 | A |
# +---+---+---+---+
# | 0 | B | C | C |

  
#   iterating for player A
# +---+---+---+---+
# | 0 | 1 | 1 | 0 |
# +---+---+---+---+
# | 0 | 2 | 2 | 0 |
# +---+---+---+---+
# | 0 | 0 | 3 | 0 |
# +---+---+---+---+
# | 0 | 0 | 0 | 0 |
  

def get_winner(players, board):
    winner = ""
    max_area = 0
    for player in players:
        area = get_max_rectangle_size(board, player)
        if area > max_area:
            max_area = area
            winner = player
    return winner

def get_max_rectangle_size(board, player):
    if not board or not board[0]:
        return 0

    rows = len(board)
    cols = len(board[0])
    # Build a heights matrix where each cell counts consecutive cells
    # (vertically) captured by the given player.
    heights = [[0] * cols for _ in range(rows)]

    # Initialize the first row.
    for c in range(cols):
        if board[0][c] == player:
            heights[0][c] = 1

    # Build the heights for the rest of the rows.
    for r in range(1, rows):
        for c in range(cols):
            if board[r][c] == player:
                heights[r][c] = heights[r - 1][c] + 1
            else:
                heights[r][c] = 0

    max_rect = 0
    # For each row, calculate the largest rectangle area in the histogram.
    for r in range(rows):
        area = get_rectangle_size(heights[r])
        max_rect = max(max_rect, area)
    return max_rect

def get_rectangle_size(row):
    n = len(row)
    left_boundary = [-1] * n
    right_boundary = [n] * n

    # Compute left boundaries:
    left_boundary[0] = -1
    for i in range(1, n):
        prev = i - 1
        while prev >= 0 and row[i] >= row[prev]:
            prev = left_boundary[prev]
        left_boundary[i] = prev

    # Compute right boundaries:
    right_boundary[n - 1] = n
    for i in range(n - 2, -1, -1):
        nxt = i + 1
        while nxt < n and row[i] >= row[nxt]:
            nxt = right_boundary[nxt]
        right_boundary[i] = nxt

    max_area = 0
    # Calculate maximum area using the boundaries.
    for i in range(n):
        area = row[i] * (right_boundary[i] - left_boundary[i] - 1)
        max_area = max(max_area, area)
    return max_area

# Sample usage
if __name__ == "__main__":
    board = [
        ["B", "A", "A", "C"],
        ["B", "A", "A", "B"],
        ["C", "C", "A", "A"],
        ["B", "B", "C", "C"]
    ]
    players = ["A", "B", "C"]
    print("The winner is:", get_winner(players, board))
