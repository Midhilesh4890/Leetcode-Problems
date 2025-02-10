#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int countWays(int n, int x, const vector<int>& coins) {
    // Initialize dp array with 0's and set dp[0] to 1
    vector<int> dp(x + 1, 0);
    dp[0] = 1;
    
    // Calculate the number of ways to form each sum up to x
    for (int i = 1; i <= x; ++i) {
        for (int coin : coins) {
            if (i >= coin) {
                dp[i] = (dp[i] + dp[i - coin]) % MOD;
            }
        }
    }
    
    return dp[x];
}

int main() {
    int n, x;
    cin >> n >> x;
    vector<int> coins(n);
    for (int i = 0; i < n; ++i) {
        cin >> coins[i];
    }
    
    // Print the result
    cout << countWays(n, x, coins) << endl;
    return 0;
}
