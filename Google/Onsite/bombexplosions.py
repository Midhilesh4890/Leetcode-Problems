# Given an array bombs, where each element is the i-th bomb's explosion radius, you can perform the following operation until all the bombs are gone:


# Choose two bombs at indices i and j which won't explode each other if detonated.
# Explode both bombs at index i and j and add the two explosion radii to the total. After this, all the bombs in the range [i - bombs[i], i + bombs[i]] and [j - bombs[j], j + bombs[j]] will be removed.
# Note that if a bomb is removed, it won't be detonated.


# Return the maximum total explosion radii you can achieve by doing this operation any amount of times until all the bombs are either detonated or removed.


# Sample Case:


# bombs = [3, 1, 1, 1, 3]
# Expected answer = 6 because you pick the first bomb and last bomb.

# After detonating the first bomb, the array becomes [0, 0, 0, 0, 3] and the total is 3
# After detonating the last bomb, the array becomes [0, 0, 0, 0, 0] and the total is 6

def max_explosion_radii(bombs):
    n = len(bombs)
    total_explosion = 0
    removed = set()  # To track removed bomb indices

    # Sort bombs by explosion radius in descending order
    indexed_bombs = sorted(enumerate(bombs), key=lambda x: -x[1])

    for i, radius in indexed_bombs:
        if i in removed:
            continue  # Skip if already removed
        
        total_explosion += radius  # Add explosion radius
        # Mark affected indices as removed
        for j in range(max(0, i - radius), min(n, i + radius + 1)):
            removed.add(j)

    return total_explosion

# Example test case
bombs = [3, 1, 1, 1, 3]
print(max_explosion_radii(bombs))  # Output: 6

def max_explosion_radii(bombs):
    """
    Calculate the maximum total explosion radii by detonating bombs optimally,
    using a union-find structure to quickly mark intervals of removed bombs.

    Args:
        bombs (List[int]): List of bomb explosion radii.

    Returns:
        int: Maximum total explosion radii.
    """
    n = len(bombs)
    total_explosion = 0
    # Create a union-find array with an extra sentinel index.
    parent = list(range(n + 1))  # parent[i] is the next unremoved index, parent[n] is a sentinel.

    def find(x):
        """
        Find the representative of x with path compression.
        This returns the smallest index >= x that has not been removed.
        """
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # Sort bombs by explosion radius in descending order along with their indices.
    indexed_bombs = sorted(enumerate(bombs), key=lambda x: -x[1])

    for i, radius in indexed_bombs:
        # If bomb i is already removed, skip it.
        if find(i) != i:
            continue

        # Detonate this bomb.
        total_explosion += radius

        # Determine the explosion interval [L, R).
        L = max(0, i - radius)
        R = min(n, i + radius + 1)

        # Use union-find to mark all indices in [L, R) as removed.
        j = find(L)
        while j < R:
            parent[j] = find(j + 1)  # Link j to the next unremoved index.
            j = parent[j]

    return total_explosion

# Example test case
bombs = [3, 1, 1, 1, 3]
print(max_explosion_radii(bombs))  # Output: 6
