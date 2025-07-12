# Given a NxN grid. Given a character 'S' (start point), character 'E' (end point), a character 'B' (Burger), and a character 'O' (Empty road). There is a person who wants to start from the starting point and wants to reach the ending point by consuming all the burgers. You need to return the minimum distance the person has to cover from start to end point by eating all the burgers. The person can travel either top, down, right, or left. Diagonal movement is not allowed. Also, the person can only reach the end point after consuming all the burgers.


# The test case is as follows:


# BOOB
# OSOO
# OOOE
# BOOO


# Expected Answer: 11


# The explanation of this test case is as follows:-
# Person initially starts at 'S' (1,1) (Initial 0 units).
# Then goes to (3,0) to eat the first burger. (now 0+3=3units).
# Then goes to (0,0) to eat the second burger (now 0+3+3=6units).
# Then goes to (0,3) to eat third burger (so now 0+3+3+3=9units).
# Then finally after eating all the burgers goes to (2,3) 'E' endpoint (so now 0+3+3+3+2=11units).
# So final answer is 11units. This is the shortest path.


# Can someone help finding the most efficient and optimised code for this problem?

from collections import deque
import sys

def min_distance(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Find positions of S, E and all burgers
    start = None
    end = None
    burgers = []
    for i in range(n):
        for j in range(m):
            ch = grid[i][j]
            if ch == 'S':
                start = (i, j)
            elif ch == 'E':
                end = (i, j)
            elif ch == 'B':
                burgers.append((i, j))
    
    # Construct our list of key nodes: index 0 is S, indices 1..k are burgers, index k+1 is E.
    nodes = [start] + burgers + [end]
    total_nodes = len(nodes)
    k = len(burgers)  # number of burgers
    
    # Precompute distances between every pair of key nodes using BFS.
    dist = [[-1] * total_nodes for _ in range(total_nodes)]
    
    def bfs(src):
        d = [[-1]*m for _ in range(n)]
        q = deque()
        r, c = src
        d[r][c] = 0
        q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and d[nr][nc] == -1:
                    d[nr][nc] = d[r][c] + 1
                    q.append((nr, nc))
        return d

    # Compute BFS from each key node and fill in our distance matrix.
    for i in range(total_nodes):
        dmap = bfs(nodes[i])
        for j in range(total_nodes):
            r, c = nodes[j]
            dist[i][j] = dmap[r][c]
    
    # If any required distance is unreachable, then it's impossible to solve.
    for i in range(total_nodes):
        for j in range(total_nodes):
            if i != j and dist[i][j] == -1:
                return -1  # or raise an error if desired
    
    # If there are no burgers, the answer is simply the distance from S to E.
    if k == 0:
        return dist[0][1]
    
    # Use bitmask DP to solve the TSP-like part:
    # dp[mask][i] is the minimum distance to have visited the set of burgers given by 'mask'
    # and currently be at node i (i=0 is S, and i from 1..k are burger nodes).
    Nmask = 1 << k
    dp = [[sys.maxsize] * (k + 1) for _ in range(Nmask)]
    dp[0][0] = 0  # starting at S with no burgers eaten
    
    # Iterate over all masks and try to take an unvisited burger next.
    for mask in range(Nmask):
        for i in range(k + 1):  # current position (S or one of the burgers)
            if dp[mask][i] != sys.maxsize:
                for j in range(1, k + 1):  # try to go to burger j
                    if not (mask & (1 << (j - 1))):  # if burger j is not visited yet
                        new_mask = mask | (1 << (j - 1))
                        dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + dist[i][j])
    
    # Finally, after all burgers have been visited, go to E (which is node k+1)
    res = sys.maxsize
    for i in range(1, k + 1):
        res = min(res, dp[Nmask - 1][i] + dist[i][k + 1])
    
    return res

# Example usage:
if __name__ == "__main__":
    grid = [
        "BOOB",
        "OSOO",
        "OOOE",
        "BOOO"
    ]
    print(min_distance(grid))  # Expected output: 11
