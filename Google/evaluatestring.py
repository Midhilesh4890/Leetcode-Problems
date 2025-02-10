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