class StreamingTicTacToe:
    def __init__(self, n):
        """
        Initialize a streaming tic-tac-toe board of size n x n.
        
        Args:
            n: Size of the board (n x n)
        """
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.input_count = 0
    
    def process_input(self, value):
        """
        Process the next input value and update the board.
        
        Args:
            value: The next input value (0 or 1)
            
        Returns:
            Boolean: True if there's a complete row or column of 1s, False otherwise
        """
        # Calculate row and column indices based on input count
        row = self.input_count // self.n
        col = self.input_count % self.n
        
        # Update the board
        self.board[row][col] = value
        
        # Increment input count for next input
        self.input_count += 1
        
        # Check if there's a complete row of 1s
        if self._check_row(row):
            return True
        
        # Check if there's a complete column of 1s
        if self._check_column(col):
            return True
        
        return False
    
    def _check_row(self, row):
        """Check if the specified row is all 1s"""
        return all(self.board[row][j] == 1 for j in range(self.n))
    
    def _check_column(self, col):
        """Check if the specified column is all 1s"""
        return all(self.board[i][col] == 1 for i in range(self.n))
    
    def print_board(self):
        """Print the current state of the board"""
        for row in self.board:
            print(row)
        print()

# Example usage:
def run_example():
    # Create a board of size 3x3
    game = StreamingTicTacToe(3)
    
    # Process inputs from the example: 0,0,1,0,0,1,0,0,0
    inputs = [0, 0, 1, 0, 0, 1, 0, 0, 0]
    
    print("Processing inputs:", inputs)
    for i, value in enumerate(inputs):
        result = game.process_input(value)
        print(f"After input {i+1} ({value}):")
        game.print_board()
        print(f"Result: {result}")
    
    # Process one more input (1) - should create a column of 1s
    final_input = 1
    print(f"Processing final input: {final_input}")
    result = game.process_input(final_input)
    print("Final board:")
    game.print_board()
    print(f"Result: {result}")  # Should be True

# Run the example
run_example()