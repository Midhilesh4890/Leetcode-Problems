def calculate_grundy(c, l):
    if c == 0:
        return 0
    grundy_set = set()
    
    # Move options: take between 1 and floor(c / l) candies
    max_take = c // l  # Maximum candies that can be taken
    take = 1
    while take <= max_take:
        grundy_set.add(calculate_grundy(c - take, l))
        take *= 2  # Jump exponentially to reduce complexity

    # Finding the minimum missing non-negative integer (Mex)
    grundy = 0
    while grundy in grundy_set:
        grundy += 1
    return grundy

def determine_winner(baskets):
    nim_sum = 0
    for candies, limit in baskets:
        grundy = calculate_grundy(candies, limit)
        nim_sum ^= grundy  # XOR all Grundy numbers
    
    return "Alice" if nim_sum != 0 else "Bob"

# Test cases
test_cases = [
    ([(8, 3), (6, 2), (5, 4)], "Alice"),
    ([(10, 4), (7, 2), (9, 3), (2, 1)], "Alice"),
    ([(12, 5), (15, 3), (14, 2)], "Alice"),
    ([(7, 3), (4, 2), (6, 5)], "Alice"),
    ([(7, 2), (1, 4), (9, 1)], "Alice"),
    ([(20, 5), (3, 7), (17, 2), (3, 4)], "Bob")
]

# Run tests
for baskets, expected in test_cases:
    result = determine_winner(baskets)
    print(f"Result: {result} | Expected: {expected} | {'Pass' if result == expected else 'Fail'}")

