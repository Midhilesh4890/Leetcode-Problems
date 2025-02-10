# Recently I came across a google interview question. The question is as follows:


# You are given two strings, P and Q consisting of characters 'a' and 'b'.


# At any given point you can perform two kind of operations on the string P:


# You either append character a to P.
# You append character b to P and then you reverse P.
# You can perform any of these operations any number of times.


# You have to tell me whether it is possible for P to be equal to Q, after performing such operations?


# An example:


# P = a, Q = baa. this will return true,
# P = b, Q = ab, this will return false

from collections import deque

def can_transform_bfs(P: str, Q: str) -> bool:
    if P == Q:
        return True

    # We'll queue up candidate strings to explore
    queue = deque([P])
    visited = set([P])

    # We only need to explore up to length of Q
    max_len = len(Q)

    while queue:
        cur = queue.popleft()

        # Generate the two possible next moves
        next1 = cur + 'a'
        if len(next1) <= max_len:
            if next1 == Q:
                return True
            if next1 not in visited:
                visited.add(next1)
                queue.append(next1)

        next2 = (cur + 'b')[::-1]  # append b, then reverse
        if len(next2) <= max_len:
            if next2 == Q:
                return True
            if next2 not in visited:
                visited.add(next2)
                queue.append(next2)

    # If we exhaust the queue, we never reached Q
    return False

# --------------------------------------------------------------------
# Example usage:
if __name__ == "__main__":
    # Example 1
    P1, Q1 = "a", "baa"
    print(can_transform_bfs(P1, Q1))  # Expected: True, because we can do:
    #   P = "a"
    #   Operation2: P + 'b' -> "ab", then reverse -> "ba"
    #   Operation1: "ba" + 'a' -> "baa"
    #
    # Example 2
    P2, Q2 = "b", "ab"
    print(can_transform_bfs(P2, Q2))  # Expected: False


def solve(P, Q):
	queue = deque([P])
	visited = {P}
	n = len(Q)

	while queue:
		word = queue.popleft()

		choice1 = word + 'a'
		choice2 = (word + 'b')[::-1]

		if len(choice1) <= n:
			if choice1 == Q:
				return True 
			if choice1 not in visited:
				visited.add(choice1)
				queue.append(choice1)

		if len(choice2) <= n:
			if choice2 == Q:
				return True 
			if choice2 not in visited:
				visited.add(choice2)
				queue.append(choice2)

	return False 




# --------------------------------------------------------------------
# Example usage:
if __name__ == "__main__":
    # Example 1
    P1, Q1 = "a", "baa"
    print(solve(P1, Q1))  # Expected: True, because we can do:
    #   P = "a"
    #   Operation2: P + 'b' -> "ab", then reverse -> "ba"
    #   Operation1: "ba" + 'a' -> "baa"
    #
    # Example 2
    P2, Q2 = "b", "ab"
    print(solve(P2, Q2))  # Expected: False





from collections import deque

def can_transform(P: str, Q: str) -> bool:
    """
    Returns True if we can transform P into Q by any sequence of:
      1) Append 'a' to the end,
      2) Append 'b' to the end and then reverse.
    Implements a BFS *backwards* from Q to see if we can reach P.
    """

    # Quick check:
    if P == Q:
        return True
    
    # We'll do a BFS starting from Q
    queue = deque([Q])
    visited = set([Q])

    # While we have candidate strings to explore
    while queue:
        cur = queue.popleft()

        # If cur == P, success
        if cur == P:
            return True

        # If cur is already shorter than P, no point exploring further
        if len(cur) < len(P):
            continue

        # -------- Reverse of operation #2 --------
        # If the string starts with 'b', then we can remove the front 'b'
        # and reverse the rest.
        if cur.startswith('b'):
            next_str = cur[1:][::-1]  # remove front 'b', then reverse
            if next_str not in visited:
                visited.add(next_str)
                queue.append(next_str)

        # -------- Reverse of operation #1 --------
        # If the string ends with 'a', then we can just remove that trailing 'a'.
        if cur.endswith('a'):
            next_str = cur[:-1]
            if next_str not in visited:
                visited.add(next_str)
                queue.append(next_str)

    # If all possibilities are exhausted and we never found P:
    return False


# --------------------------------------------------------------------
# DEMO
if __name__ == "__main__":
    # Example 1 (from the problem statement):
    # P = "a", Q = "baa" => True
    # Explanation (forward):
    #   a -> append b -> "ab" -> reverse -> "ba" -> append a -> "baa"
    P1, Q1 = "a", "baa"
    print(can_transform(P1, Q1))  # Expected True

    # Example 2 (from the problem statement):
    # P = "b", Q = "ab" => False
    P2, Q2 = "b", "ab"
    print(can_transform(P2, Q2))  # Expected False
