from collections import deque

def find_highest_water_tower(heights, town1, town2):
    m, n = len(heights), len(heights[0])

    visited_from_town1 = [[False] * n for _ in range(m)]
    visited_from_town2 = [[False] * n for _ in range(m)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start, visited):
        queue = deque([start])
        r0, c0 = start
        visited[r0][c0] = True

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # Note: >= instead of <=
                    if heights[nr][nc] >= heights[r][c]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

    # 1) BFS from each town allowing movement to neighbors of equal/greater height
    bfs(tuple(town1), visited_from_town1)
    bfs(tuple(town2), visited_from_town2)

    # 2) Find the highest cell that both BFS traversals could reach
    max_height = -1
    best_location = None

    for i in range(m):
        for j in range(n):
            if visited_from_town1[i][j] and visited_from_town2[i][j]:
                if heights[i][j] > max_height:
                    max_height = heights[i][j]
                    best_location = [i, j]

    return best_location


# --------------------------
# Test cases
# --------------------------
heights1 = [
    [4, 9, 7, 6, 5],
    [2, 6, 5, 4, 3],
    [6, 5, 1, 2, 8],
    [3, 4, 7, 2, 5]
]
town1_1 = [1, 4]  # (row=1, col=4)
town1_2 = [3, 1]  # (row=3, col=1)

print(find_highest_water_tower(heights1, town1_1, town1_2))
# Example expected: [0, 1] or whichever is the highest valid common cell.


heights2 = [
    [9, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 1, 0]
]
town2_1 = [1, 3]
town2_2 = [2, 3]

print(find_highest_water_tower(heights2, town2_1, town2_2))
# Example expected: [2, 2] or [0,0] if that can reach both, etc.
