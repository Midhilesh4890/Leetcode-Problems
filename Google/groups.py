# Do let me know , if you have seen this question before and how would you solve this and what could be most optimised solution tc and sc for same.


# I was able to code with tc: O(mn + nlogn) and sc: O(mn)
# I'm not sure if any other more optimised solution exists.


# You are given a list of items grouped into sections, each of equal size. The first input is a 2D array where each sub-array represents a section with the item numbers. For example, {{2, 2, 6}, {1, 3, 4}, {2, 3, 4}}.


# You need to reorganize the items such that each section has the item numbers in ascending order, with no repeated item numbers within a section. The structure must be preserved, meaning the number of sections and the number of items per section should remain unchanged.


def counting_sort_deduplicate(sections, max_value):
    result = []
    
    for section in sections:
        seen = [False] * (max_value + 1)  # Boolean array for seen numbers
        sorted_section = []
        
        # Mark seen numbers
        for num in section:
            if not seen[num]:
                seen[num] = True
        
        # Append numbers in sorted order
        for num in range(max_value + 1):
            if seen[num]:
                sorted_section.append(num)
        
        result.append(sorted_section)
    
    return result

# Example Usage:
sections = [[2, 2, 6], [1, 3, 4], [2, 3, 4]]
max_value = max(max(sublist) for sublist in sections)  # Get max value in input
result = counting_sort_deduplicate(sections, max_value)
print(result)  # Output: [[2, 6], [1, 3, 4], [2, 3, 4]]
