import os, sys
from math import *
from collections import *
from bisect import *
from operator import * 
from itertools import *
from functools import *
 
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
 
 
## Sieve for Prime Factorization when limit <= 10**6
 
def factorization():
    P = 10**6
    primes = list(range(P + 1))
    for i in range(2, P + 1):
        if primes[i] == i:
            for j in range(i * i, P + 1, i):
                primes[j] = i
 

def solve(N, A):
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
        while A[i] % 3 == 0:
            A[i] = A[i] // 3
    return 'Yes' if len(set(A)) == 1 else 'No'

    

if __name__ == '__main__':
    for _ in range(int(input())):
        N = iip()
        A = li()
        print(solve(N, A))





    