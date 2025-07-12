# question: palindromic triples
# given a string S , 3 palindromes (start(i),end(j)) such that i1<=j1<i2<=j2<i3<=j3 .
# return how many such palindromic triples present.


# answer will be long long int


# constriants:
# 1<len<1e5
# S contains lower case letters

def count_palindromic_triples(S):
    n = len(S)
    
    # Step 1: Identify all palindromic substrings using dynamic programming
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True
    
    for i in range(n-1):
        if S[i] == S[i+1]:
            dp[i][i+1] = True
    
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if S[i] == S[j] and dp[i+1][j-1]:
                dp[i][j] = True
    
    palindromes = []
    
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                palindromes.append((i, j))
    
    # Step 3: Count the number of valid triples
    count = 0
    m = len(palindromes)
    
    # Create arrays to store the count of valid (i, j) pairs
    right_count = [0] * m
    for k in range(m):
        i2, j2 = palindromes[k]
        for l in range(k+1, m):
            i3, j3 = palindromes[l]
            if i2 <= j2 < i3 <= j3:
                right_count[k] += 1
    
    # Count the number of valid triples
    for i in range(m):
        i1, j1 = palindromes[i]
        for j in range(i+1, m):
            i2, j2 = palindromes[j]
            if i1 <= j1 < i2 <= j2:
                count += right_count[j]
    
    return count

s = "ababa"
print(count_palindromic_triples(s))  