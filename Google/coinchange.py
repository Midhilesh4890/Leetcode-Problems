# coinchane but reverse we will be given dp but we need to find coins
def recover_coins(dp, target):
    coins = []
    # dp is a list of length target+1; dp[0] must be 1.
    while any(dp[i] != 0 for i in range(1, target+1)):
        # Find smallest i > 0 with dp[i] > 0
        coin = next(i for i in range(1, target+1) if dp[i] > 0)
        coins.append(coin)
        # "Remove" coin's contribution: new_dp[j] = dp[j] - (dp[j-coin] if j>=coin else 0)
        new_dp = dp.copy()
        for j in range(coin, target+1):
            new_dp[j] = dp[j] - dp[j-coin]
        dp = new_dp
    return coins

# For the given example:
dp = [1, 0, 1, 0, 1, 1, 2, 1, 2, 1, 3]
target = 10
print(recover_coins(dp, target))  # Output: [2, 5, 6]
