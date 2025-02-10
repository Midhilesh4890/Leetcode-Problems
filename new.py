MOD = 10**9 + 7

def count_ways(n, x, coins):
    # Initialize dp array with 0's and set dp[0] to 1
    dp = [0] * (x + 1)
    dp[0] = 1
    
    # Calculate the number of ways to form each sum up to x
    for i in range(1, x + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = (dp[i] + dp[i - coin]) % MOD
    
    return dp[x]

# Example usage
n, x = map(int, input().split())
coins = list(map(int, input().split()))

# Print the result
print(count_ways(n, x, coins))
