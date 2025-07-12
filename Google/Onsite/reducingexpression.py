def simplify(expression):
    """
    Simplifies an algebraic expression by combining like terms.
    
    Args:
        expression (str): An algebraic expression with variables, +, -, and parentheses
        
    Returns:
        str: The simplified expression
    """
    # Dictionary to store the coefficient of each variable
    coefficients = {}
    
    # Parse the expression using a sign multiplier to handle nested parentheses
    i = 0
    sign_stack = [1]  # Start with positive sign
    current_sign = 1
    
    while i < len(expression):
        char = expression[i]
        
        if char == '+':
            # Next term will be added
            current_sign = sign_stack[-1]
            
        elif char == '-':
            # Next term will be subtracted
            current_sign = -sign_stack[-1]
            
        elif char == '(':
            # Push the current sign to stack for the terms inside parentheses
            sign_stack.append(current_sign * sign_stack[-1])
            current_sign = sign_stack[-1]  # Reset current sign
            
        elif char == ')':
            # Pop the sign from stack when exiting parentheses
            sign_stack.pop()
            current_sign = sign_stack[-1]  # Reset to the parent context's sign
            
        elif 'a' <= char <= 'z':
            # For variables, update their coefficients in the dictionary
            # Check for coefficient numbers before the variable
            coef = 1
            # Variable is already processed with the current sign
            coefficients[char] = coefficients.get(char, 0) + (coef * current_sign)
            
        # Move to the next character
        i += 1
    
    # Build the result string
    result = ""
    
    # Sort variables for consistent output
    for var in sorted(coefficients.keys()):
        coef = coefficients[var]
        if coef == 0:
            continue  # Skip terms with zero coefficient
            
        if coef > 0:
            # Add + sign for positive terms (except the first term)
            if result:
                result += "+"
                
            # Don't show coefficient 1
            if coef == 1:
                result += var
            else:
                result += f"{coef}{var}"
                
        elif coef < 0:
            # For negative coefficients
            if coef == -1:
                result += f"-{var}"
            else:
                result += f"{coef}{var}"
    
    return result if result else "0"  # Return "0" for empty result

def main():
    print(simplify("a-(a+b)"))  # Expected: -b
    print(simplify("a-(b+c-(d))"))  # Expected: a-b-c+d
    print(simplify("-(b+c)-b"))  # Expected: -2b-c
    print(simplify("a+a+a+a-(b+c)"))  # Expected: 4a-b-c
    print(simplify("-(a-(b-c)+d)"))  # Expected: -a+b-c-d

if __name__ == "__main__":
    main()