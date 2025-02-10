# Given two lists of Strings with the same set of elements and no duplicates within the list, find out the minimum number of contiguous swaps that are required to get from one list to another.
# Example S = [B,C,A,D] and D = [C,D,A,B]


# B C A D
# C B A D
# C A B D
# C A D B
# C D A B


# contiguous swaps means - you can only swap adjacent elements.


# Basically minimum number of swaps required is same as the inversions right 
# inversion means when i < j and arr[i] > arr[j]


def count_inversions(arr):
	if len(arr) <= 1:
		return arr, 0 

	mid = len(arr) // 2 

	left, leftinv = count_inversions(arr[:mid])
	right, rightinv = count_inversions(arr[mid:])
	merged, mergeinv = modified_merge_sort(left, right)

	return merged, mergeinv + leftinv + rightinv

def modified_merge_sort(left, right):

	i, j = 0, 0
	merged = []
	inversions = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			merged.append(left[i])
			i += 1

		else:
			merged.append(right[j])
			inversions += len(left) - i
			j += 1 

	merged.extend(left[i:])
	merged.extend(right[j:])

	return merged, inversions

def min_contiguous_swaps(source, destination):
    # Create a mapping from each element in the destination list to its index.
    index_map = {element: i for i, element in enumerate(destination)}
    
    # Map the source list into a list of indices according to the destination order.
    permutation = [index_map[element] for element in source]
    
    # The number of inversions in 'permutation' equals the minimum number of swaps needed.
    _, inversion_count = count_inversions(permutation)
    return inversion_count



if __name__ == "__main__":
    # Example 1:
    source1 = ["B", "C", "A", "D"]
    destination1 = ["C", "D", "A", "B"]
    swaps1 = min_contiguous_swaps(source1, destination1)
    print(f"Minimum contiguous swaps required (Example 1): {swaps1}")
    
    # Example 2:
    source2 = ["B", "D", "A", "E", "C"]
    destination2 = ["A", "B", "C", "D", "E"]
    swaps2 = min_contiguous_swaps(source2, destination2)
    print(f"Minimum contiguous swaps required (Example 2): {swaps2}")


# from sortedcontainers import SortedList

# def count_inversions_sortedcontainers(arr):
#     """
#     Count the number of inversions in the list 'arr' using a SortedList.
#     For each element, count how many of the previously seen elements are greater than it.
#     """
#     inversions = 0
#     sorted_list = SortedList()
    
#     # Process each element in the array
#     for x in arr:
#         # bisect_right returns the insertion position of x in sorted_list such that
#         # all elements to its right are greater than x.
#         pos = sorted_list.bisect_right(x)
#         # The number of elements after pos in sorted_list are those larger than x,
#         # each of which forms an inversion with x.
#         inversions += len(sorted_list) - pos
#         # Add the current element into the sorted list.
#         sorted_list.add(x)
    
#     return inversions

# def min_contiguous_swaps(source, destination):
#     """
#     Given two lists of strings (source and destination) with the same set of unique elements,
#     returns the minimum number of contiguous (adjacent) swaps needed to transform the source
#     list into the destination list.
#     """
#     # Map each element in destination to its index.
#     index_map = {element: idx for idx, element in enumerate(destination)}
    
#     # Convert the source list into a permutation of indices according to destination's order.
#     permutation = [index_map[element] for element in source]
    
#     # Count inversions in this permutation using the sortedcontainers approach.
#     return count_inversions_sortedcontainers(permutation)

# if __name__ == "__main__":
#     # Example 1
#     source1 = ["B", "C", "A", "D"]
#     destination1 = ["C", "D", "A", "B"]
#     swaps1 = min_contiguous_swaps(source1, destination1)
#     print(f"Minimum contiguous swaps required (Example 1): {swaps1}")
    
#     # Example 2
#     source2 = ["B", "D", "A", "E", "C"]
#     destination2 = ["A", "B", "C", "D", "E"]
#     swaps2 = min_contiguous_swaps(source2, destination2)
#     print(f"Minimum contiguous swaps required (Example 2): {swaps2}")
