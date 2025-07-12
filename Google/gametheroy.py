# The interviewer asked me how I would rate myself in problem-solving. I said 6/10. Then he asked if I was familiar with game theory. I replied, 'Alright, I haven't done many problems, but I could try.' Then he gave me this problem.


# Problem:
# Alice and Bob are playing a game with candy baskets. Initially, there are N baskets, and the i-th basket has candies_in_basket_i candies and a special number candies_limit_i.


# The game starts with Alice, and they take turns. On each turn, the player picks a basket and takes away some candies. If the player chooses the i-th basket and there are candies_left_in_basket_i candies, they must take between 1 and floor(candies_left_in_basket_i / candies_limit_i) candies.


# The player who can't make a move (because all baskets are empty or they can't take the required number of candies) loses the game. Both Alice and Bob play perfectly, so they always make the best possible moves.


# Your task is to determine who will win the game, assuming both play optimally.


# 8 3
# 6 2
# 5 4
# Expected: Alice


# 10 4
# 7 2
# 9 3
# 2 1
# Expected: Alice


# 12 5
# 15 3
# 14 2
# Expected: Alice


# 7 3
# 4 2
# 6 5
# Expected: Alice


# 7 2
# 1 4
# 9 1
# Expected: Alice

# 20 5
# 3 7
# 17 2
# 3 4
# Expected: Bob
# After struggling a bit, I solved it with a time complexity of nearly O(N⋅max(candies_in_basket_i)). However, the interviewer mentioned that candies_in_basket_i and candies_limit_i could be really large. Then I was able to solve it in O(N⋅log(max(candies_in_basket_i))), and the interviewer was happy.


# To my surprise, the next day, I was told that the interviewer wasn't happy about that he had to mention of large constraints. Nevertheless, I qualified for the onsite round. Let's see what happens!


# Could someone suggest what to study and where to prepare?

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

