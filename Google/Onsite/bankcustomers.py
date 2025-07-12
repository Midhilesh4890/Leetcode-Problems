# # There is a bank which has a fund of X dollars. The bank has to serve N customers one by one who may either deposit/withdraw money.
# # The bank must stop serving any more customers if it meets a customer with withdrawal request exceeding the current funds.


# # Also, the bank has the power to refuse service to any number of customers but once the bank starts from any arbitrary customer,
# # it continues serving each customer after that customer and can only stop if it is unable to make a withdrawal request greater than the bank's funds at that point of time.


# # What is the maximum number of people the bank can serve?


# # First line will contain bank's initial fund: X
# # Second line will contain number of customers: N
# # Each of the next N lines contain a possible transaction: R. If R is negative, then it is a deposit to the bank, else it is a withdrawal.


# # constraints - n <=10^5

# def max_customers_served(X, transactions):
#     N = len(transactions)
#     left = 0
#     max_served = 0
#     current_funds = 0  # To track funds after picking a starting point

#     for right in range(N):
#         current_funds += transactions[right]

#         while current_funds < 0 and left <= right:  # If withdrawal exceeds funds, move left pointer
#             current_funds -= transactions[left]
#             left += 1

#         max_served = max(max_served, right - left + 1)  # Update maximum count

#     return max_served

# # Input handling
# X = 10
# transactions = [-2, 5, -3, 6, 4, -1, 7]

# # Output the result
# print(max_customers_served(X, transactions))
# X = 1
# transactions = [1, -3, 5, -2, 1]
# print(max_customers_served(X, transactions))


import math

def max_customers_served(X, transactions):
    n = len(transactions)
    m = n + 1  # Length of prefix sum array Q
    # Build prefix sum array Q such that Q[0] = 0 and Q[i+1] = Q[i] + transactions[i]
    Q = [0] * m
    for i in range(n):
        Q[i + 1] = Q[i] + transactions[i]
    
    # Build Sparse Table for range minimum queries on Q.
    log = [0] * (m + 1)
    for i in range(2, m + 1):
        log[i] = log[i // 2] + 1

    k = log[m] + 1  # Number of levels
    st = [[0] * m for _ in range(k)]
    # Level 0 of the sparse table: just the array Q itself.
    for i in range(m):
        st[0][i] = Q[i]
    
    j = 1
    while (1 << j) <= m:
        for i in range(m - (1 << j) + 1):
            st[j][i] = min(st[j - 1][i], st[j - 1][i + (1 << (j - 1))])
        j += 1

    # Function to query the minimum in Q from index L to R (inclusive)
    def query_min(L, R):
        length = R - L + 1
        j = log[length]
        return min(st[j][L], st[j][R - (1 << j) + 1])
    
    max_served = 0
    # For each starting index i (which means before serving customer i, with initial funds X)
    # the condition for serving customers from i to j is:
    #   X + (Q[t] - Q[i]) >= 0  for all t in [i+1, j+1]
    # Equivalently: Q[t] >= Q[i] - X.
    for i in range(m):
        threshold = Q[i] - X
        lo, hi = i + 1, m - 1
        best = i  # best valid index found in Q (if best remains i, no customer is served)
        while lo <= hi:
            mid = (lo + hi) // 2
            if query_min(i + 1, mid) >= threshold:
                best = mid  # mid is valid, try to extend further
                lo = mid + 1
            else:
                hi = mid - 1
        served = best - i  # served customers count = (j+1) - i, i.e. j - i + 1
        if served > max_served:
            max_served = served
    
    return max_served


# Example usage:
if __name__ == "__main__":
    X = 10
    transactions = [-5, 20, -1, -2, 3, -4]
    print(max_customers_served(X, transactions))

    # Input handling
    X = 10
    transactions = [-2, 5, -3, 6, 4, -1, 7]

    # Output the result
    print(max_customers_served(X, transactions))
    X = 1
    transactions = [1, -3, 5, -2, 1]
    print(max_customers_served(X, transactions))
