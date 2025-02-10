from collections import deque

def neighbors(s):
    """
    Generate all valid strings that can be reached from s in one move.
    A move consists of changing one letter at a time.
    We must ensure that after the change no two adjacent characters are equal.
    """
    n = len(s)
    for i in range(n):
        for c in "xyz":
            if c == s[i]:
                continue  # No change.
            # Check that changing s[i] to c does not break the rule.
            if i > 0 and s[i-1] == c:
                continue
            if i < n - 1 and s[i+1] == c:
                continue
            # Build the new string.
            yield s[:i] + c + s[i+1:]

def min_moves(start, target):
    """
    Returns the minimum number of operations to transform start into target.
    Both start and target are valid strings (no two consecutive letters the same).
    """
    if start == target:
        return 0
    queue = deque([start])
    # Use a dictionary to keep track of the number of moves (distance) to each state.
    dist = {start: 0}
    
    while queue:
        current = queue.popleft()
        for nb in neighbors(current):
            if nb not in dist:
                dist[nb] = dist[current] + 1
                if nb == target:
                    return dist[nb]
                queue.append(nb)
    # Should not happen if the reconfiguration graph is connected.
    return -1

if __name__ == '__main__':
    examples = [
        ("zxyz", "zyxz"),
        ("xyzyzyxyzx", "xzyzyzyxzy"),
        ("xyxyxyxyxy", "xzyxyxzyxz"),
        ("xyxyzyzyxy", "zyzyxzyzyz"),
        ("xzxyxyzyzyxyzx", "zyzyxzyzyzyxzy")
    ]
    
    for start, target in examples:
        moves = min_moves(start, target)
        print(f"Transforming {start} -> {target} requires {moves} moves.")
