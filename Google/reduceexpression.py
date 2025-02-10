# Calculator to reduce expression
# a + a * 4 - b + c + 3 * b

# 5a +2b +c


# from collections import defaultdict

# def helper(s, start, c, mp):
#     i = start
#     n = len(s)
#     num = 1
#     variable = None
    
#     while i < n and s[i] not in ['+', '-']:
#         if 'a' <= s[i] <= 'z':
#             variable = s[i]
#             i += 1
#             continue
#         if s[i] == '*':
#             i += 1
#             continue
        
#         t = 0
#         while i < n and '0' <= s[i] <= '9':
#             t = t * 10 + int(s[i])
#             i += 1
#         num *= t
    
#     if c == '-':
#         num *= -1
    
#     if variable is not None:
#         mp[variable] += num
    
#     if i < n:
#         helper(s, i + 1, s[i], mp)

# def reduce_exp(s):
#     mp = defaultdict(int)
#     helper(s, 0, '+', mp)
    
#     ans = ""
#     for variable, coeff in sorted(mp.items()):
#         if coeff == 0:
#             continue
#         if ans and coeff > 0:
#             ans += '+'
#         ans += f"{coeff}{variable}"
    
#     return ans if ans else "0"


# s = 'a + a * 4 - b + c + 3 * b'
# print(reduce_exp(s))


def simplify_expression(expr):
    # Split the expression into tokens by whitespace.
    # For the sample input, tokens will be:
    # ['a', '+', 'a', '*', '4', '-', 'b', '+', 'c', '+', '3', '*', 'b']
    tokens = expr.split()
    
    # Dictionary to hold the combined coefficient for each term.
    # We use the variable part (as a string) as the key. For constant terms, the key will be ''.
    result = {}

    i = 0
    current_sign = 1  # Overall sign for the current term

    # Helper function to check if a token represents a number.
    def is_number(s):
        return s.lstrip('-').isdigit()

    # Process the tokens one term at a time.
    while i < len(tokens):
        token = tokens[i]

        # If the token is an operator, update the current sign accordingly.
        if token == '+':
            current_sign = 1
            i += 1
            continue
        elif token == '-':
            current_sign = -1
            i += 1
            continue

        # Otherwise, we are at the start of a term (which may be a multiplication chain).
        coef = 1       # Start with an implicit coefficient of 1.
        var_list = []  # List to store variable factors (if any).

        # Process the multiplication chain until we hit a '+' or '-' or run out of tokens.
        while i < len(tokens) and tokens[i] not in ['+', '-']:
            # Skip over the multiplication operator.
            if tokens[i] == '*':
                i += 1
                continue

            factor = tokens[i]
            # If the factor is a number, multiply it into the coefficient.
            if is_number(factor):
                coef *= int(factor)
            else:
                # Assume the factor is a variable (or a string representing a variable).
                # For a more general solution (e.g. "a * b") you might sort or combine factors.
                var_list.append(factor)
            i += 1

        # To have a canonical form, sort the variable factors.
        var_list.sort()
        # Create a key from the variable part. If no variable appears, we treat it as a constant term.
        key = ''.join(var_list)  # e.g., 'a' or 'ab' etc.

        # The term's final coefficient includes the current sign.
        term_coef = current_sign * coef

        # Add the term into our result dictionary, combining like terms.
        result[key] = result.get(key, 0) + term_coef

        # After finishing a term, the sign will be reset by the next operator token.
    
    # Build the final expression string.
    # We want to output constant terms (key == '') at the end.
    # Sort the keys: variables (alphabetically) first, then constants.
    keys = sorted(result.keys(), key=lambda k: (k == '', k))

    # Prepare a list to hold string representations of each nonzero term.
    output_terms = []
    for k in keys:
        coef = result[k]
        if coef == 0:
            continue  # Skip any terms that cancel out.
        
        # For constant terms (where k is an empty string), just use the coefficient.
        if k == '':
            term_str = str(coef)
        else:
            # If the coefficient is 1 or -1, we omit the 1.
            if coef == 1:
                term_str = k
            elif coef == -1:
                term_str = '-' + k
            else:
                term_str = str(coef) + k
        output_terms.append(term_str)

    # If no terms remain, the result is 0.
    if not output_terms:
        return "0"

    # Now join the terms into one string.
    # The first term is added as-is, and subsequent terms get a '+' or '-' appropriately.
    result_str = output_terms[0]
    for term in output_terms[1:]:
        if term[0] == '-':
            result_str += " - " + term[1:]
        else:
            result_str += " + " + term

    return result_str

# Example usage:
if __name__ == '__main__':
    expr = "a + a * 4 - b + c + 3 * b"
    simplified = simplify_expression(expr)
    print(simplified)  # Expected output: 5a + 2b + c
