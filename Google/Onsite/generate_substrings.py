# Given a string, your task is to generate a list of substrings such that while appending all of the substrings in the list should give back the original string. If the resulting substring is not already present in the list, it should be added to the list.


# Examples:


# Input: "GOOOOOOGLE"
# Output: ["G", "O", "OO", "OOO", "GL", "E"]


# Input: "GOOOOOOGLEG"
# Output: ["G", "O", "OO", "OOO", "GL", "E", "G"]
# handling edge case

class Solution:
    def maxUniqueSplit(self, s: str) -> tuple[int, list[str]]:
        # A set to track substrings that have been used
        seen = set()
        
        # A list to keep track of the maximum count of unique substrings
        # Using a list to allow modification inside the recursive function
        max_count = [0]
        
        # A list to store the best split resulting in the maximum unique substrings
        best_split = [[]]
        
        # Start the backtracking process
        self.backtrack(s, 0, seen, 0, max_count, [], best_split)
        
        # Return the maximum count and the corresponding best split
        return max_count[0], best_split[0]

    def backtrack(self, s, start, seen, count, max_count, current_split, best_split):
        # Pruning: If the current count plus the remaining characters cannot exceed max_count, stop exploring
        if count + (len(s) - start) <= max_count[0]:
            return
        
        # If the end of the string is reached, check if the current split is better than the best so far
        if start == len(s):
            if count > max_count[0]:
                max_count[0] = count  # Update the maximum count
                best_split[0] = current_split[:]  # Update the best split (make a copy of the current split)
            return
        
        # Try splitting the string at every possible position
        for end in range(start + 1, len(s) + 1):
            sub_string = s[start:end]  # Get the substring from the current start to the end index
            
            # If the substring is not already used in the current split, explore further
            if sub_string not in seen:
                seen.add(sub_string)  # Mark the substring as used
                current_split.append(sub_string)  # Add the substring to the current split
                
                # Recursively explore the next part of the string
                self.backtrack(s, end, seen, count + 1, max_count, current_split, best_split)
                
                # Backtrack: Remove the last substring and unmark it in `seen` for the next iteration
                current_split.pop()
                seen.remove(sub_string)
        
        # No explicit return needed, as this is void for recursive exploration
        return