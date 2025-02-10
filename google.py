def mock_query(L, R):
    return 1 in A[L:R+1]

def find_ones_positions(M, query):
    positions = []
    start = 0
    while start < M:
        if not query(start, M - 1):
            break
        left, right = start, M - 1
        while left < right:
            mid = (left + right) // 2
            if query(left, mid):
                right = mid
            else:
                left = mid + 1
        positions.append(left)
        start = left + 1
    return positions

# Test cases
A = [0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
result = find_ones_positions(len(A), mock_query)
print(result)  # Expected: [1, 2, 9]

# Additional test cases
A = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
result = find_ones_positions(len(A), mock_query)
print(result)  # Expected: [4, 7]

A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = find_ones_positions(len(A), mock_query)
print(result)  # Expected: []

A = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
result = find_ones_positions(len(A), mock_query)
print(result)  # Expected: [0, 9]

#--------------------------------------------------------------#

def eval_expr(expr):
    """
    Evaluates an expression of the form func(arg1, arg2),
    where func is one of: add, sub, mul, div, pow.
    Nested calls are supported, e.g. add(5, mul(2, pow(5,2))).
    """
    expr = expr.strip()
    
    # Base case: if no parentheses, treat it as a number
    if '(' not in expr:
        return float(expr)  # or int(expr) if you need integers only

    # 1) Split on the first '(' to get the function name
    func, inside = expr.split('(', 1)
    func = func.strip()

    # 2) The part inside parentheses is everything until the matching ')'
    #    We assume the expression is well-formed so just drop the last char ')'
    inside = inside[:-1].strip()  # remove the trailing ')'

    # 3) Split arguments by commas at top-level (depth=0)
    args = []
    depth = 0
    start = 0
    for i, ch in enumerate(inside):
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        elif ch == ',' and depth == 0:
            args.append(inside[start:i].strip())
            start = i + 1
    # Append the final argument
    args.append(inside[start:].strip())

    # 4) Recursively evaluate each argument
    values = [eval_expr(a) for a in args]

    # 5) Apply the operation based on 'func'
    if func == 'add': return values[0] + values[1]
    if func == 'sub': return values[0] - values[1]
    if func == 'mul': return values[0] * values[1]
    if func == 'div': return values[0] / values[1]  # float division
    if func == 'pow': return values[0] ** values[1]

    # If the function is not recognized, raise an error
    raise ValueError(f"Unknown function '{func}'")


# --------------------------------------------------------------------
# Test the eval_expr function with several expressions
def main():
    test_expressions = [
        "add(1,2)",
        "sub(10,3)",
        "mul(4,5)",
        "div(20,4)",
        "pow(2,4)",
        "add(5, mul(2, pow(5,2)))",  # nested example
        "sub(pow(2,3), mul(2,3))",   # 2^3 - (2*3)
        "div(add(10,20), mul(2,5))"  # (10+20) / (2*5)
    ]

    for expr in test_expressions:
        result = eval_expr(expr)
        print(f"{expr} = {result}")

if __name__ == "__main__":
    main()

#---------------------------------------------------------------
try:
    from sortedcontainers import SortedDict
except ImportError:
    raise ImportError("Please install sortedcontainers via 'pip install sortedcontainers' to run this example.")

class IntervalContainerSortedDict:
    def __init__(self):
        # Key: interval start, Value: interval end
        # Intervals are [start, end), and non-overlapping
        self.intervals = SortedDict()

    def InsertRange(self, start, end):
        """
        Inserts [start, end), merging overlaps in O(log n + k)
        where k is number of intervals merged.
        """
        if start >= end:
            return

        # We'll accumulate the final merged [merged_start, merged_end)
        merged_start, merged_end = start, end

        # 1) Find interval that might overlap from the left:
        # 'floor_key' means the greatest key <= start (if any).
        it = self.intervals.irange(maximum=start, reverse=True)  # "reverse" to get floor
        try:
            prev_key = next(it)
        except StopIteration:
            prev_key = None

        if prev_key is not None:
            prev_end = self.intervals[prev_key]
            # if there's an overlap or adjacency, merge with the previous interval
            if prev_end >= start:  # overlap or abut
                merged_start = min(merged_start, prev_key)
                merged_end = max(merged_end, prev_end)
                # remove that interval
                del self.intervals[prev_key]
                prev_key = None

        # 2) Merge all intervals that start <= merged_end
        # We'll collect keys to remove in a list to avoid changing dict while iterating
        to_remove = []
        for key in self.intervals.irange(merged_start, merged_end):
            curr_end = self.intervals[key]
            if key <= merged_end:  # Overlap
                merged_end = max(merged_end, curr_end)
                to_remove.append(key)
            else:
                break

        # Remove all overlapped intervals
        for key in to_remove:
            del self.intervals[key]

        # 3) Insert the merged interval
        self.intervals[merged_start] = merged_end

    def Query(self, point):
        """
        Returns True if 'point' lies in any of our intervals, else False.
        Time Complexity: O(log n).
        """
        # We want the interval whose start is the floor key for 'point'
        # i.e. the largest key <= point
        idx = self.intervals.bisect_right(point) - 1
        if idx < 0:
            return False
        start_key = self.intervals.keys()[idx]   # the start
        end_val = self.intervals[start_key]      # the end
        return (start_key <= point < end_val)

# Example usage:
if __name__ == "__main__":
    container = IntervalContainerSortedDict()
    container.InsertRange(2, 3)
    container.InsertRange(2, 5)   # merges => [2,5)
    container.InsertRange(9, 13)  # => [[2,5), [9,13)]
    container.InsertRange(3, 7)   # merges => [2,7), [9,13)]
    print("\nBalanced BST (SortedDict) Query:")
    print(container.Query(0))   # False
    print(container.Query(2))   # True
    print(container.Query(6))   # True
    print(container.Query(10))  # True
#----------------------------------------------
def count_valid_tuples(array_A, array_B, array_C, threshold_B, threshold_C, distance):
  
    left_B = 0
    right_B = 0
    left_C = 0
    right_C = 0
    valid_tuples_count = 0 

  
    for value_A in array_A:
        # Move left_B to the first position where B[left_B] + distance >= value_A
        while left_B < len(array_B) and array_B[left_B] + distance < value_A:
            left_B += 1

        # Move right_B to the first position where B[right_B] + threshold_B > value_A
        while right_B < len(array_B) and array_B[right_B] + threshold_B <= value_A:
            right_B += 1

        # Move left_C to the first position where C[left_C] + distance >= value_A
        while left_C < len(array_C) and array_C[left_C] + distance < value_A:
            left_C += 1

        # Move right_C to the first position where C[right_C] + threshold_C > value_A
        while right_C < len(array_C) and array_C[right_C] + threshold_C <= value_A:
            right_C += 1

  
        valid_tuples_count += (right_B - left_B) * (right_C - left_C)

    return valid_tuples_count  


def main():
    array_A = [0, 1]
    array_B = [0, 1]
    array_C = [0, 1]
    distance = 1  

    total_valid_tuples = (
        count_valid_tuples(array_A, array_B, array_C, 0, 0, distance)
        + count_valid_tuples(array_B, array_C, array_A, 0, 1, distance)
        + count_valid_tuples(array_C, array_A, array_B, 1, 1, distance)
    )

    print(total_valid_tuples)  


if __name__ == "__main__":
    main()

def count_tuples(A, B, C, D):
    n = len(A)  # Each of A, B, C is length n
    
    #--- Step 1: 3-Way Merge in O(n) ---
    merged = []
    i = j = k = 0
    while i < n or j < n or k < n:
        # Among A[i], B[j], C[k], pick the smallest
        candidates = []
        if i < n: candidates.append((A[i], 'A'))
        if j < n: candidates.append((B[j], 'B'))
        if k < n: candidates.append((C[k], 'C'))
        
        val, origin = min(candidates, key=lambda x: x[0])
        merged.append((val, origin))
        
        if origin == 'A':
            i += 1
        elif origin == 'B':
            j += 1
        else:
            k += 1
    
    #--- Step 2: Sliding Window in O(n) ---
    L = 0
    countA = countB = countC = 0
    ans = 0
    n_merged = len(merged)  # should be 3n

    for R in range(n_merged):
        # Shrink [L..R] if it exceeds the D range
        while merged[R][0] - merged[L][0] > D:
            # remove merged[L] from window
            if merged[L][1] == 'A':
                countA -= 1
            elif merged[L][1] == 'B':
                countB -= 1
            else:
                countC -= 1
            L += 1
        
        # Count new triples formed by merged[R]
        origin_R = merged[R][1]
        if origin_R == 'A':
            ans += countB * countC
        elif origin_R == 'B':
            ans += countA * countC
        else:  # 'C'
            ans += countA * countB
        
        # Now add merged[R] into the window
        if origin_R == 'A':
            countA += 1
        elif origin_R == 'B':
            countB += 1
        else:
            countC += 1
    
    return ans
    
A = [0, 1]
B = [0, 1]
C = [0, 1]
D = 1

print(count_tuples(A, B, C, D))

#-----------------------------------#
