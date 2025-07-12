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