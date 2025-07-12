# Calculator to do add, sub, divide, modulus, multiply and power operations
# add(5, sub(pow(7, 2), mul(3, 2)))

def evaluateString(S):

    if not S:
        return 0

    def evaluate(operator, operand1, operand2):
        if operator == "add":
            return operand1 + operand2
        if operator == "sub":
            return operand1 - operand2
        if operator == "mul":
            return operand1 * operand2
        if operator == "pow":
            return operand1**operand2

    index = 0
    stack = []
    while index < len(S):
        char = S[index]
        if char in " (,":
            index += 1
            continue
        if char.isdigit():
            start = index
            while index + 1 < len(S) and S[index + 1].isdigit():
                index += 1
            index += 1
            stack.append(int(S[start:index]))
        if char.isalpha():
            start = index
            end = index + 2
            operator = S[start : end + 1]
            stack.append(operator)
            index = end + 1
        if char == ")":
            operand2 = stack.pop()
            operand1 = stack.pop()
            operator = stack.pop()
            stack.append(evaluate(operator, operand1, operand2))
            index += 1
    return stack[0]

S = 'add(5, sub(pow(7, 2), mul(3, 2)))'
print(evaluateString(S))



def evaluate_expression(expression):
    def evaluate(operator, operand1, operand2):
        if operator == "add":
            return operand1 + operand2
        if operator == "sub":
            return operand1 - operand2
        if operator == "mul":
            return operand1 * operand2
        if operator == "pow":
            return operand1 ** operand2
        if operator == "div":
            return operand1 / operand2
        
    def parse_number(s, index):
        num_str = ""
        while index < len(s) and (s[index].isdigit() or s[index] in "-+eE."):
            num_str += s[index]
            index += 1
        
        # Check for valid scientific notation (exponent should be an integer)
        if 'e' in num_str.lower():
            parts = num_str.lower().split('e')
            if len(parts) != 2 or not parts[1].lstrip('-+').isdigit():
                raise ValueError(f"Invalid scientific notation: {num_str}")
        
        return float(num_str), index
    
    index = 0
    stack = []
    
    while index < len(expression):
        char = expression[index]
        
        if char in " (,":
            index += 1
            continue
        
        if char.isalpha():  # Parsing operators
            operator = expression[index:index+3]
            stack.append(operator)
            index += 3
        
        elif char.isdigit() or char in "-+.":  # Parsing numbers (including floats and scientific notation)
            try:
                number, new_index = parse_number(expression, index)
                stack.append(number)
                index = new_index
            except ValueError as e:
                print(f"Error: {e}")
                return None
        
        elif char == ")":  # Evaluate expressions
            if len(stack) < 3:
                print("Error: Malformed expression")
                return None
            operand2 = stack.pop()
            operand1 = stack.pop()
            operator = stack.pop()
            stack.append(evaluate(operator, operand1, operand2))
            index += 1
    
    return stack[0] if stack else None

# Test cases
expressions = [
    "add(1,2)",
    "mul(2e3, sub(4,2))",
    "add(2.4, pow(2,4e4.5))",  # This should return an error message
    "add(5, sub(pow(7, 2), mul(3, 2)))"
]

for expr in expressions:
    result = evaluate_expression(expr)
    if result is not None:
        print(f"{expr} = {result}")
