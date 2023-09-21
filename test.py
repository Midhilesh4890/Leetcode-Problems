import os, sys
from math import *
from collections import *
from bisect import *
from operator import * 
from itertools import *
from functools import *
import re
 
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
 
def factorization():
    P = 100
    primes = list(range(P + 1))
    for i in range(2, P + 1):
        if primes[i] == i:
            for j in range(i * i, P + 1, i):
                primes[j] = i

    return primes

def prime_factors_count(n, primes):
    factors_count = defaultdict(int)  # Dictionary to store prime factors and their counts

    # Divide n by the smallest prime factors until n becomes 1
    while n > 1:
        smallest_prime = primes[n]
        factors_count[smallest_prime] += 1
        n //= smallest_prime

    return sum(factors_count.values())

def sieve():
    n = 3000
    primes = [False, False] + [True] * (n - 2)

    for i in range(2, isqrt(n) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return [index for index, val in enumerate(primes) if val]

def solve(S):
    pass

if __name__ == '__main__':
    S = ip()
    print(solve(S))
