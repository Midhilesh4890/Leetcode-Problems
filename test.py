import os, sys
from math import *
from collections import *
from bisect import *
from operator import * 
from itertools import *
from functools import *
import re
<<<<<<< HEAD
from heapq import *
 
#path
try:
    sys.stdin = open('D:\\Projects\\DSA Practice\\inp.txt','r')
    sys.stdout = open('D:\\Projects\\DSA Practice\\out.txt','w')
except: pass
 
# Inputs
string_input = lambda: input()
integer_input = lambda: int(input())
list_of_integers = lambda: list(map(int, input().split()))
list_of_strings  = lambda: list(map(str, input().split()))
list_of_floats  = lambda: list(map(float, input().split()))
=======
 
#path
try:
    sys.stdin = open('D:\\DSA Practice\\inp.txt','r')
    sys.stdout = open('D:\\DSA Practice\\out.txt','w')
except: pass
 
# Inputs
ip  = lambda: input()
iip = lambda: int(input())
li  = lambda: list(map(int, input().split()))
ls  = lambda: list(map(str, input().split()))
>>>>>>> 9114eae875aaed33928084dcaa0407f354290f1a
 
MOD = 1000000007
 
#Binary Index Tree or Fenwick Tree
class BinaryIndexTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.a, self.tree = [0] * (self.n + 1), [0] * (self.n + 1)
 
        # # Construction of BIT
        # for i in range(self.n):
        #   k = i + 1
        #   while k <= self.n:
        #     self.tree[k] += nums[i]
        #     k += (k & -k)
 
        for index,val in enumerate(nums):
            self.update(index,val)
 
    def update(self, i, val):
 
        diff, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.tree[i] += diff
            i += (i & -i)
  
    def getSum(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.tree[i]
            i -= (i & (-i))
        return res
     
    def sumRange(self, i, j):
        return self.getSum(j) - self.getSum(i-1)
 
 
# Segment Tree
class SegmentTree:
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0]*self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
      
    def update(self, i, val):
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n>>1] = self.tree[n] + self.tree[n^1]
            n >>= 1
    
    def sumRange(self, i, j):
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 ==0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res
<<<<<<< HEAD

def find_factors(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return list(factors)

def prime_factorization(P):
=======
 
def factorization():
    P = 100
>>>>>>> 9114eae875aaed33928084dcaa0407f354290f1a
    primes = list(range(P + 1))
    for i in range(2, P + 1):
        if primes[i] == i:
            for j in range(i * i, P + 1, i):
                primes[j] = i

    return primes

<<<<<<< HEAD
def prime_factors_using_sieve(n):
    primes = sieve_of_eratosthenes(int(n**0.5) + 1)
    factors = []
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n //= p
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return factors

=======
>>>>>>> 9114eae875aaed33928084dcaa0407f354290f1a
def prime_factors_count(n, primes):
    factors_count = defaultdict(int)  # Dictionary to store prime factors and their counts

    # Divide n by the smallest prime factors until n becomes 1
    while n > 1:
        smallest_prime = primes[n]
        factors_count[smallest_prime] += 1
        n //= smallest_prime

    return sum(factors_count.values())

<<<<<<< HEAD
def sieve_of_eratosthenes(n):
=======
def sieve():
    n = 3000
>>>>>>> 9114eae875aaed33928084dcaa0407f354290f1a
    primes = [False, False] + [True] * (n - 2)

    for i in range(2, isqrt(n) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
<<<<<<< HEAD
            
    return [index**2 for index, val in enumerate(primes) if val]


def isPrime(n):
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

def sum_of_divisors_sieve_1_to_N(N):
    div_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            div_sum[j] += i
    return div_sum

def compute_prefix_function(pattern):
    m = len(pattern)
    prefix_function = [0] * m
    l = 0

    for r in range(1, m):
        while l > 0 and pattern[r] != pattern[l]:
            l = prefix_function[l - 1]

        if pattern[r] == pattern[l]:
            l += 1

        prefix_function[r] = l

    return prefix_function

def kmp_count_occurrences(text, pattern):
    n, m = len(text), len(pattern)
    prefix_function = compute_prefix_function(pattern)
    j = 0
    count = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_function[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            count += 1
            j = prefix_function[j - 1]

    return count

def sum_of_digits(number):
    digit_sum = 0

    # Iterate through the digits using a while loop
    while number > 0:
        # Get the last digit by taking the remainder when divided by 10
        last_digit = number % 10
        # Add the last digit to the sum
        digit_sum += last_digit
        # Remove the last digit from the number
        number = number // 10  # Integer division to remove the last digit

    return digit_sum

def digitdp(S, pos, tight, dp, flag):
    num_digits = len(S)

    # Base case: If we have processed all digits
    if pos == num_digits:
        return 1 if flag == 1 else 0

    # If the result for this state is already calculated, return it
    elif dp[pos][flag][tight] != -1:
        return dp[pos][flag][tight]

    if tight == 1:
        res = 0
        for i in range(int(S[pos]) + 1):
            temp = flag
            if i == 3:
                temp = 1
            if i == int(S[pos]):
                res += digitdp(S, pos + 1, 1, dp, temp)
            else:
                res += digitdp(S, pos + 1, 0, dp, temp)
        dp[pos][flag][tight] = res
        return res
    else:
        res = 0
        for i in range(10):
            temp = flag
            if i == 3:
                temp = 1
            res += digitdp(S, pos + 1, 0, dp, temp)
        dp[pos][flag][tight] = res
        return res

def isPerfectSquare(num):
    l = 1
    r = int(sqrt(num)) + 1

    while l <= r:
        mid = (l + r) >> 1

        if mid * mid == num: return True

        elif mid * mid < num: l = mid + 1

        else: r = mid - 1

    return False

def ispowerof2(n):
    # positive
    n = abs(n)
    return not (n & n - 1) 

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def sieve(max_val):
    smallest_prime = list(range(max_val + 1))
    for i in range(2, int(max_val**0.5) + 1):
        if smallest_prime[i] == i:
            for j in range(i * i, max_val + 1, i):
                if smallest_prime[j] == j:
                    smallest_prime[j] = i
    return smallest_prime

def factorize(x, smallest_prime):
    factors = []
    while x > 1:
        prime = smallest_prime[x]
        count = 0
        while x % prime == 0:
            count += 1
            x //= prime
        factors.append((prime, count))
    return factors

MAX_VAL = 200000
smallest_prime = sieve(MAX_VAL)

def solve(n, arr):
    prime_freq = defaultdict(int)  
    square_freq = defaultdict(int)  
    product_freq = defaultdict(int)

    for num in arr:
        factors = factorize(num, smallest_prime)
        if len(factors) == 1:
            prime, exp = factors[0]
            if exp == 1:
                prime_freq[prime] += 1
            elif exp == 2:
                square_freq[prime] += 1
        elif len(factors) == 2:
            if factors[0][1] == 1 and factors[1][1] == 1:
                p, q = factors[0][0], factors[1][0]
                if p > q:
                    p, q = q, p
                product_freq[(p, q)] += 1

    total_primes = sum(prime_freq.values())
    sum_squares = sum(val * val for val in prime_freq.values())
    pairs_pq = (total_primes * total_primes - sum_squares) // 2

    for (p, q), cnt in product_freq.items():
        pairs_pq += prime_freq.get(p, 0) * cnt + prime_freq.get(q, 0) * cnt + (cnt * (cnt + 1)) // 2

    pairs_p2 = 0
    for p, cnt in square_freq.items():
        pairs_p2 += prime_freq.get(p, 0) * cnt + (cnt * (cnt + 1)) // 2

    total_pairs = pairs_pq + pairs_p2
    return total_pairs


if __name__ == "__main__":
    T = integer_input()
    for _ in range(T):
        n = integer_input()
        a = list_of_integers()
        print(solve(n, a))

=======
    return [index for index, val in enumerate(primes) if val]

def solve(S):
    pass

if __name__ == '__main__':
    S = ip()
    print(solve(S))
>>>>>>> 9114eae875aaed33928084dcaa0407f354290f1a
