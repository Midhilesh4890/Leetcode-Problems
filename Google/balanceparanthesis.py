# You are given a string containing only parentheses ('(' and ')') and digits (0-9). At the index of a digit, you must delete a number of parentheses to the left of the index equal to the digit's value. Return true if it is possible to balance the parenthesis of the input.

# Example 1 Input: ((2)) Output: False Reason: Only possible string is unbalanced: "))"

# Example 2 Input: ((((2)) Output: True Reason: Only possible string is balanced: "(())"

# Example 3 Input: (()1(1)) Output: True Reason: Multiple possible strings and one is balanced: ")())", "(())", "()))".

# Background: 

# 1.Digits should not be included in the result string, although that doesn't matter for calculating the boolean result.

# 2.If a digit doesn't have enough characters to the left to delete, then return false.


def can_balance_parentheses(s: str) -> bool:
    stack = []
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Store index of '('
        elif char.isdigit():
            remove_count = int(char)
            if len(stack) < remove_count:  # Not enough '(' to remove
                return False
            for _ in range(remove_count):
                stack.pop()  # Remove the required '('
    
    # Finally, check if the remaining parentheses form a balanced string
    return len(stack) % 2 == 0

# Test cases
print(can_balance_parentheses("((2))"))  # False
print(can_balance_parentheses("((((2))"))  # True
print(can_balance_parentheses("(()1(1))"))  # True
