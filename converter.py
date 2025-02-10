def series(n):
    dp = [0, 1]
    mod = 1000000007
    if n == 1: return dp
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] % mod + dp[i - 2] % mod
    
    return dp

print(series(5))