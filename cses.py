from typing import List

def check(s: str) -> int:
    last = [0, 0]
    dp = 1
    for c in s:
        dp = dp * 2 - last[int(c)]
        last[int(c)] = dp
    return dp - 1

def gcd_len(a: int, b: int) -> int:
    ans = -1
    while b:
        d, r = divmod(a, b)
        ans += d
        a, b = b, r
    return ans if a == 1 else float('inf')

def trace(a: int, b: int) -> str:
    ret = []
    curr = 1
    while b:
        d, r = divmod(a, b)
        ret.append(str(curr) * d)
        a, b = b, r
        curr = 1 - curr
    return ''.join(ret)[:-1]

def solve(n: int) -> str:
    len_val, a = n + 1, 1
    n += 2
    for i in range(n // 2, 1, -1):
        x = gcd_len(n - i, i)
        if x < len_val:
            len_val, a = x, i
    return trace(n - a, a)

if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
