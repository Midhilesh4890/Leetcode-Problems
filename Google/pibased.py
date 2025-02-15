def findMatchingIndices(pi: str) -> list[int]:
    result = []
    n = len(pi)

    def checkMultiDigitMatch(index: int) -> bool:
        index_str = str(index)
        index_len = len(index_str)

        # Ensure the full index string fits within `pi`
        if index - 1 + index_len > n:
            return False

        # Check if the substring in `pi` matches `index`
        for i, digit in enumerate(index_str):
            if pi[index - 1 + i] != digit:
                return False
        return True

    for i in range(1, n + 1):
        if checkMultiDigitMatch(i):
            result.append(i)

    return result

# Example Test
pi = "314159265359"
print(findMatchingIndices(pi))  # Expected Output: [4, 5, 6, 9]
