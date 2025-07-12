def find_subsequence_index(A, B):
    n = len(A)
    m = len(B)
    
    # If B is empty, we can decide what to return (here, 1)
    if m == 0:
        return 1
    
    # Try each occurrence of B[0] in A as a potential starting point.
    # Note: The first character must match exactly.
    for start in range(n):
        if A[start] != B[0]:
            continue
        
        used_substitution = False  # No substitution used yet.
        pos = start               # Current position in A where we matched the last character.
        valid = True              # Assume we can match the rest of B.
        
        # Try to match the rest of B (from index 1 onward)
        for j in range(1, m):
            candidate = -1        # candidate index for substitution (if needed)
            found_exact = False   # flag to indicate an exact match for B[j]
            
            # Look for a match for B[j] in A after the current position.
            for k in range(pos + 1, n):
                if A[k] == B[j]:
                    # Found an exact match.
                    found_exact = True
                    pos = k
                    break
                elif candidate == -1 and not used_substitution:
                    # Record the first possible candidate for substitution.
                    candidate = k
            
            # If no exact match was found...
            if not found_exact:
                if candidate != -1 and not used_substitution:
                    # Use our one allowed substitution and set pos to the candidate.
                    used_substitution = True
                    pos = candidate
                else:
                    # We couldn’t match B[j] (and substitution is either not available or no candidate exists).
                    valid = False
                    break
        
        if valid:
            # Found a valid subsequence starting at 'start'
            return start + 1  # Return 1-indexed position.
    
    return -1

# Test cases:
print(find_subsequence_index("abcbc", "cbe"))  # Expected output: 3
print(find_subsequence_index("lhs", "rhs"))    # Expected output: -1
