from sortedcontainers import SortedList

def find_leftmost_smaller_sortedlist(arr):
    seen = SortedList()
    result = []
    
    for num in arr:
        idx = seen.bisect_left(num)  # Find the leftmost smaller element
        if idx == 0:
            result.append(-1)
        else:
            result.append(seen[idx - 1])
        
        seen.add(num)  # Insert current number in sorted order
    
    return result
arr = [2, 1, 3, 2, 1, 3]
m = max(arr)

print(find_leftmost_smaller_sortedlist(arr))  # Output: [-1, -1, 2, 1, -1, 2]
