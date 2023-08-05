import sys
from collections import defaultdict, deque
from copy import deepcopy
from itertools import combinations
from math import ceil, floor

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 18
MOD = 998244353

def _3Dto1D(i, j, k, j_max, k_max):
    return i * j_max * k_max + j * k_max + k

def _1Dto3D(i, j_max, k_max):
    return i // j_max // k_max, i % j_max // k_max, i % k_max

def _2Dto1D(i, j, j_max):
    return i * j_max + j

def _1Dto2D(i, j_max):
    return i // j_max, i % j_max

def _grid2D(i, j, init=0):
    return [[init for _ in range(j)] for _ in range(i)]

def _grid3D(i, j, k, init=0):
    return [[[init for _ in range(k)] for _ in range(j)] for _ in range(i)]

def _repr2D(grid):
    for g in grid: print(g)
    print("")

def bit_count(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

def compress(arr):
    p, r = {}, {}
    for i, a in enumerate(sorted(list(set(arr)))):
        p[a] = i
        r[i] = a
    return p, r

def bfs_grid(si, sj, grid) -> list:
    """ 障害物の存在するグリッドで各マスへの最短到達距離を返す """
    dist = [[INF for _ in range(_)] for _ in range(_)]
    que = deque([(si, sj)])
    while que:
        i, j = que.popleft()
        dij = dist[i][j]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == ".":
                if dist[ni][nj] > d + 1:
                    dist[ni][nj] = dij + 1
                    que.append((ni, nj))
    return dist

def factorization(n):
    """ factorization(n) = [{p1: r1}, {p2: r2}, ...] : O(n^1/2) """
    arr = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt
    if temp!=1:
        arr[temp] = 1
    if arr==[]:
        arr[n] = 1
    return arr

class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.log = n.bit_length()
        self.data = [0] * n
 
    def __sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
 
    def add(self, p, x):
        """ a[p] += xを行う"""
        p += 1
        while p <= self.n:
            self.data[p - 1] += x
            p += p & -p
 
    def sum(self, l, r):
        """ a[l] + a[l+1] + .. + a[r-1]を返す"""
        return self.__sum(r) - self.__sum(l)
 
    def lower_bound(self, x):
        """a[0] + a[1] + .. a[i] >= x となる最小のiを返す"""
        if x <= 0:
            return -1
        i = 0
        k = 1 << self.log
        while k:
            if i + k <= self.n and self.data[i + k - 1] < x:
                x -= self.data[i + k - 1]
                i += k
            k >>= 1
        return i
 
    def _repr(self):
        res = [self.sum(i, i+1) for i in range(self.n)]
        return " ".join(map(str, res))

class Graph(object):
    def __init__(self, edge, direction=0):
        self.graph = [[] for _ in range(N)]
        for u, v in edge:
            self.graph[u - 1].append(v - 1)
            if not direction:
                self.graph[v - 1].append(u - 1)
                
    def bipartile(self, start):
        """
            start から塗り始めて 2部グラフ かどうかを判定
            ->  is_bipartile:    bool
                is_bipartile が True のとき
                ->  color:           {頂点1: 1, 頂点2: 2, ...}
                    color_count:     {1: n1, 2: n2}
        """
        is_bipartile = True
        color = defaultdict(int)
        color_count = defaultdict(int)
        stack = [start]
        color[start] = 1
        color_count[1] = 1
        while stack:
            i = stack.pop()
            for j in self.graph[i]:
                if color[j] == color[i]:
                    return False, color, color_count
                if color[j]:
                    continue
                stack.append(j)
                color[j] = 2 if color[i] == 1 else 1
                color_count[color[j]] += 1
        return True, color, color_count

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def _repr(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

# _ = input()
# _ = int(input())
# _, _ = map(int, input().split())
# _ = list(map(int, input().split()))
# _ = [input() for _ in range(_)]
# _ = [list(map(int, input().split())) for _ in range(_)]

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

p, r = compress(A)
A = [p[a] for a in A]

answer = []
bit0 = FenwickTree(N + 1)
bit1 = FenwickTree(N + 1)
for i in range(M):
    bit0.add(A[i], 1)
    bit1.add(A[i], r[A[i]])
idx = bit0.lower_bound(K)
answer.append(bit1.sum(0, idx + 1) - (bit0.sum(0, idx + 1) - K) * r[idx])

for i in range(M, N):
    bit0.add(A[i], 1)
    bit1.add(A[i], r[A[i]])
    bit0.add(A[i - M], -1)
    bit1.add(A[i - M], -r[A[i - M]])
    idx = bit0.lower_bound(K)
    answer.append(bit1.sum(0, idx + 1) - (bit0.sum(0, idx + 1) - K) * r[idx])
    
print(*answer)