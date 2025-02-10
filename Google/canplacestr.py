def can_place_string(matrix, s):
    """
    Return True if string s can be placed in matrix according to the rules:
      1) s must lie contiguously in one row or one column
      2) Can't cross '#' cells
      3) Spaces can be overwritten, existing letters must match exactly
      4) No leading/trailing free space (boundary must be '#' or edge)
    """
    r = len(matrix)
    c = len(matrix[0]) if r > 0 else 0

    # 1) Check each row
    for row_idx in range(r):
        row_string = build_wildcard_string(matrix[row_idx])
        if kmp_wildcard_search(row_string, s):
            return True

    # 2) Check each column
    #    Build each column as a list of chars, then convert to wildcard string
    for col_idx in range(c):
        col_cells = [matrix[row][col_idx] for row in range(r)]
        col_string = build_wildcard_string(col_cells)
        if kmp_wildcard_search(col_string, s):
            return True

    return False

def build_wildcard_string(cells):
    """
    Given a list of cells (each cell is ' ', '#', or a letter),
    build a string where:
      '#' -> '|'
      ' ' -> '?'
      letter -> the same letter
    """
    out = []
    for ch in cells:
        if ch == '#':
            out.append('|')
        elif ch == ' ':
            out.append('?')
        else:
            # assume it's a letter
            out.append(ch)
    return ''.join(out)

def kmp_wildcard_search(text, pattern):
    """
    Return True if 'pattern' can be matched (contiguously) somewhere in 'text'
    with the rules:
      - text_char == '?' matches any single character in pattern
      - otherwise text_char must match pattern_char exactly
      - must respect the 'no leading/trailing space' rule, i.e.
         the match cannot be preceded or followed by a non-'|' in the text
         => text[pos-1] == '|' (or pos-1 < 0) AND text[pos+len(pattern)] == '|' (or out of range)

    We do a standard KMP match, but "character equality" is replaced by a wildcard match.
    As soon as we find a valid match, we check boundary conditions and if satisfied, return True.
    If no match satisfies the boundary conditions, return False.
    """

    n = len(pattern)
    m = len(text)
    if n == 0:
        return False  # trivial: no empty patterns to place

    # Precompute the partial match (pi) array for the pattern under normal (exact) match,
    # but we'll do the "wildcard" check only at search-time, not at pattern-time.
    # For the pattern itself, building the usual prefix function is straightforward.
    pi = build_prefix_function(pattern)

    # KMP search with wildcard check
    j = 0  # index in pattern
    for i in range(m):  # i - index in text
        # While there's a mismatch (under wildcard rules), move j via pi-table
        while j > 0 and not chars_match(text[i], pattern[j]):
            j = pi[j-1]

        # If matches (under wildcard rule), advance j
        if chars_match(text[i], pattern[j]):
            j += 1

        # If we've matched the entire pattern
        if j == n:
            # End position in text is i (0-based), so start is i-n+1
            start = i - n + 1
            end = i  # inclusive
            # boundary check:
            #   text[start-1] should be '|' or out of range
            #   text[end+1]   should be '|' or out of range
            if (start == 0 or text[start-1] == '|') and (end == m-1 or text[end+1] == '|'):
                return True
            # If boundary fails, continue searching
            # Move j for the next potential match
            j = pi[j-1]

    return False

def chars_match(tc, pc):
    if tc == '?':
        return True
    return tc == pc

def build_prefix_function(pattern):
    """
    Standard KMP prefix function for the pattern itself (exact match).
    """
    n = len(pattern)
    pi = [0]*n
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

if __name__ == "__main__":
    # Example 1 from the question:
    matrix1 = [
        ["#", " ", "#"],
        [" ", " ", "#"],
        ["#", "c", " "]
    ]
    s1 = "abc"
    print(can_place_string(matrix1, s1))  # Expect True

    # Example 2 from the question:
    matrix2 = [
        [" ", " "],
        [" ", " "]
    ]
    s2 = "a"
    print(can_place_string(matrix2, s2))  # Expect False
