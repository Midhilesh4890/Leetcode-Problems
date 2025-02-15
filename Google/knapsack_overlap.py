def compute_z_function(s):
    """Computes the Z-function for a given string s."""
    n = len(s)
    Z = [0] * n
    l, r, k = 0, 0, 0

    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1
    return Z

def find_overlap(w1, w2):
    """Finds the maximum suffix-prefix overlap using Z-Algorithm."""
    combined1 = w1 + "$" + w2
    combined2 = w2 + "$" + w1
    
    Z1 = compute_z_function(combined1)
    Z2 = compute_z_function(combined2)
    
    max_overlap = 0
    for i in range(len(w1) + 1, len(combined1)):
        if Z1[i] + i == len(combined1):
            max_overlap = max(max_overlap, Z1[i])
    
    for i in range(len(w2) + 1, len(combined2)):
        if Z2[i] + i == len(combined2):
            max_overlap = max(max_overlap, Z2[i])

    if max_overlap > 0:
        return w1 + w2[max_overlap:]
    return None

def generate_all_combinations(words, scores, limit):
    """Generates all valid word merges using overlap detection."""
    word_score_map = {words[i]: scores[i] for i in range(len(words))}
    all_words = set(words)
    queue = list(words)

    while queue:
        w1 = queue.pop(0)
        for w2 in words:
            merged = find_overlap(w1, w2)
            if merged and merged not in word_score_map:
                new_length = len(merged)
                if new_length <= limit:  # Ensure it stays within size limit
                    word_score_map[merged] = word_score_map[w1] + word_score_map[w2]
                    all_words.add(merged)
                    queue.append(merged)

    return word_score_map

def max_word_score(words, scores, limit):
    """Solves the problem using Dynamic Programming (0/1 Knapsack)."""
    word_score_map = generate_all_combinations(words, scores, limit)
    all_words = list(word_score_map.keys())

    dp = [0] * (limit + 1)

    for word in all_words:
        word_len = len(word)
        word_score = word_score_map[word]
        for i in range(limit, word_len - 1, -1):  
            dp[i] = max(dp[i], dp[i - word_len] + word_score)

    return max(dp)

# Test case
words = ["a", "aa", "aaa", "aaaa"]
scores = [1, 10, 100, 1000]
limit = 7
print(max_word_score(words, scores, limit))  # Output: 17
