import re

def validate_equation(equation):
    def is_valid_expression(expression):
        # Check for invalid characters
        if not re.fullmatch(r"[a-z+\-() ]*", expression):
            return False
        
        # Check for balanced parentheses
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        if stack:  # Unmatched parentheses
            return False
        
        # Check for invalid patterns
        if re.search(r"(^[+\-])|([+\-]{2,})|([+\-]$)", expression):  # Leading/trailing/consecutive operators
            return False
        
        return True
    
    # Split into LHS and RHS
    parts = equation.split('=')
    if len(parts) != 2:  # Equation must have exactly one '='
        return "Invalid"
    
    lhs, rhs = parts
    lhs, rhs = lhs.strip(), rhs.strip()  # Trim spaces
    
    if not lhs or not rhs:  # Both sides must be non-empty
        return "Invalid"
    
    # Validate both sides
    if is_valid_expression(lhs) and is_valid_expression(rhs):
        return "Valid"
    else:
        return "Invalid"

# Test cases
test_cases = [
    "a + x = b + (c + a)",  # Valid
    "a + x =",              # Invalid
    "a + -x = a + b"        # Invalid
]

for test in test_cases:
    print(f"{test} -> {validate_equation(test)}")
