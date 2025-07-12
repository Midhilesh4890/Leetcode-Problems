# Given an array with N integers, starting index S and a value X. You are playing game in which you start from S and first move is always odd. If the move is odd you can jump to first index on the left which has value A[idx]+1. If the move is even you the same on right side. Whenever we make a jump update the previous position by X. Output the end position when you can not make any jump. If the game is going to be infinite return -1 or return the end index.


# From example


# A = [3,4,2,2,7]
# X = 4
# S=2


# we are at index 2, A[2] = 2; move is odd 2+1=3 exists at index 0 Array will become this
# 3,4,6,2,7
# Now we are at index 0, make a jump because 4 exists on right (even move)


# 7,4,6,2,7
# Now at index 1 4+1 5 doesnt exist on the right of 5


# Answer is 1 final index.


# A = [2,1]
# X = 2
# S = 1


# This is an infinite case.
def game_end_position(A, S, X):
    n = len(A)
    move = 1  # move counter (1-indexed: odd moves then even moves)
    current = S
    seen_states = set()
    
    # Helper functions: search left and search right
    def find_first_left(idx, target):
        for j in range(idx-1, -1, -1):
            if A[j] == target:
                return j
        return -1

    def find_first_right(idx, target):
        for j in range(idx+1, n):
            if A[j] == target:
                return j
        return -1

    while True:
        # Create a state tuple: (tuple version of A, current index, move parity)
        # (Using tuple(A) as the array state; in a real scenario, you might need a more efficient cycle check.)
        state = (tuple(A), current, move % 2)
        if state in seen_states:
            return -1  # Infinite loop detected
        seen_states.add(state)

        current_value = A[current]
        required_value = current_value + 1
        
        if move % 2 == 1:
            # Odd move: search to the left.
            next_index = find_first_left(current, required_value)
        else:
            # Even move: search to the right.
            next_index = find_first_right(current, required_value)
        
        # If no valid jump exists, return the current index.
        if next_index == -1:
            return current
        
        # Before jumping, update the current cell.
        A[current] += X
        # Move to the next index.
        current = next_index
        move += 1

# --- Example runs ---
# Example 1:
A1 = [3, 4, 2, 2, 7]
S1 = 2
X1 = 4
result1 = game_end_position(A1.copy(), S1, X1)
print("Final index for Example 1:", result1)  # Expected output: 1

# Example 2:
A2 = [2, 1]
S2 = 1
X2 = 2
result2 = game_end_position(A2.copy(), S2, X2)
print("Final index for Example 2:", result2)  # Expected output: -1 (infinite loop)
