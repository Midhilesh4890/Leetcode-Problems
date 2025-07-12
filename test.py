import sys
from collections import *
from itertools import *
from math import *
from heapq import *
from functools import *
import os
from bisect import *

# Set input and output paths
try:
    sys.stdin = open('D:\\Projects\\DSA Practice\\inp.txt', 'r')
    sys.stdout = open('D:\\Projects\\DSA Practice\\out.txt', 'w')
except FileNotFoundError:
    pass

# Input functions
si = lambda: input().strip()
ii = lambda: int(input().strip())
li = lambda: list(map(int, input().split()))
ls = lambda: input().split()
MOD = 1000000007

# Binary Indexed Tree (Fenwick Tree)
class BinaryIndexTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.a, self.tree = [0] * (self.n + 1), [0] * (self.n + 1)
        for index, val in enumerate(nums):
            self.update(index, val)

    def update(self, i, val):
        diff, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.tree[i] += diff
            i += (i & -i)

    def get_sum(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res
    
    def sum_range(self, i, j):
        return self.get_sum(j) - self.get_sum(i - 1)

# Segment Tree
class SegmentTree:
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
    
    def update(self, i, val):
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1
    
    def sum_range(self, i, j):
        m, n = self.l + i, self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res

# Utility Functions
def find_factors(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return list(factors)

def sieve(limit):
    primes = list(range(limit + 1))
    for i in range(2, int(limit**0.5) + 1):
        if primes[i] == i:
            for j in range(i * i, limit + 1, i):
                primes[j] = i
    return primes

def count_factors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1 if i == n // i else 2
    return count


def prime_factors_count(n, primes):
    factors_count = defaultdict(int)
    while n > 1:
        smallest_prime = primes[n]
        factors_count[smallest_prime] += 1
        n //= smallest_prime
    return sum(factors_count.values())

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def modular_exponentiation(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

def is_perfect_square(num):
    return int(sqrt(num)) ** 2 == num

def solve(N):
    MOD = 998244353
    N %= MOD
    res = 0
    for num in range(3, N + 1):
        if is_power_of_2(N):
            res += N - 2
            res % MOD

        else:
            res += num - count_factors(num)
            res % MOD

    return res % MOD

if __name__ == '__main__':
    N = ii()
    print(solve(N))