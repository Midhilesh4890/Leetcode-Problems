def max_number_with_cost(cost, budget):
    # Find the minimum cost and its corresponding digit
    min_cost = min(cost)
    min_digit = cost.index(min_cost) + 1  # Digit corresponding to min cost

    # Maximum length we can afford with the minimum cost digit
    max_length = budget // min_cost
    if max_length == 0:
        return "0"  # Not enough budget for even one digit

    # Initialize result with the smallest digit that fits the budget
    result = [min_digit] * max_length
    budget -= min_cost * max_length

    # Try to replace digits starting from the most significant position
    for i in range(max_length):
        for d in range(9, min_digit, -1):
            extra_cost = cost[d - 1] - min_cost
            if budget >= extra_cost:
                result[i] = d
                budget -= extra_cost

    return "".join(map(str, result))

# Test case
cost = [4, 3, 4, 1, 7, 8, 2, 3, 4]
budget = 15
print(max_number_with_cost(cost, budget))  # Expected output: "666666666666666"
