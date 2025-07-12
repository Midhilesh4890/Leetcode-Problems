# Mock query function
def mock_query(L, R):
    return 1 in A[L:R+1]

# 1️⃣ Recursive Approach
def find_ones_recursive(start, end, query, positions):
    if start > end or not query(start, end):
        return
    if start == end:
        positions.append(start)
        return
    mid = (start + end) // 2
    find_ones_recursive(start, mid, query, positions)
    find_ones_recursive(mid + 1, end, query, positions)

def find_ones_positions_recursive(M, query):
    positions = []
    find_ones_recursive(0, M - 1, query, positions)
    return positions

# 2️⃣ Divide & Conquer Approach
def find_ones_divide_conquer(start, end, query):
    if start > end or not query(start, end):
        return []
    if start == end:
        return [start]

    mid = (start + end) // 2
    left_positions = find_ones_divide_conquer(start, mid, query)
    right_positions = find_ones_divide_conquer(mid + 1, end, query)
    return left_positions + right_positions

def find_ones_positions_divide_conquer(M, query):
    return find_ones_divide_conquer(0, M - 1, query)

# 3️⃣ Binary Search Approach
def find_ones_binary_search(M, query):
    positions = []
    start = 0
    while start < M:
        if not query(start, M - 1):
            break
        left, right = start, M - 1
        while left < right:
            mid = (left + right) // 2
            if query(left, mid):
                right = mid
            else:
                left = mid + 1
        positions.append(left)
        start = left + 1
    return positions

# Test case
A = [0, 1, 1, 0, 0, 0, 0, 0, 0, 1]  # Expected output: [1, 2, 9]

# Running all approaches
print("Recursive Approach:", find_ones_positions_recursive(len(A), mock_query))  # Expected: [1, 2, 9]
print("Divide & Conquer Approach:", find_ones_positions_divide_conquer(len(A), mock_query))  # Expected: [1, 2, 9]
print("Binary Search Approach:", find_ones_binary_search(len(A), mock_query))  # Expected: [1, 2, 9]
