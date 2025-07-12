from collections import deque
import heapq

def find_minimum_electricity_network(grid):
    """
    Find the minimum cost electricity network that connects all cities.
    
    Args:
        grid: 2D list where:
             1 = road (can build on)
             0 = farm (cannot build on)
            -1 = city (need to connect)
            
    Returns:
        2D list representing the electricity network
    """
    rows, cols = len(grid), len(grid[0])
    
    # Find all cities
    cities = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == -1:
                cities.append((i, j))
    
    # If no cities, return empty grid
    if not cities:
        return [row[:] for row in grid]
    
    # Find shortest paths between all pairs of cities using BFS
    paths = {}
    for i, (city_row, city_col) in enumerate(cities):
        city_key = (city_row, city_col)
        paths[city_key] = {}
        
        for j, (target_row, target_col) in enumerate(cities):
            if i != j:
                target_key = (target_row, target_col)
                path = find_shortest_path(grid, city_row, city_col, target_row, target_col)
                
                if path:
                    paths[city_key][target_key] = path
    
    # Create minimum spanning tree using Kruskal's algorithm
    mst = find_minimum_spanning_tree(cities, paths)
    
    # Create result grid with the minimum spanning tree
    result_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Mark all cities in the result grid
    for row, col in cities:
        result_grid[row][col] = -1
    
    # Mark all edges in the minimum spanning tree
    for path in mst:
        for row, col in path:
            # Don't overwrite cities
            if grid[row][col] != -1:
                result_grid[row][col] = 1
    
    return result_grid

def find_shortest_path(grid, start_row, start_col, end_row, end_col):
    """
    Find the shortest path between two cities using BFS.
    """
    rows, cols = len(grid), len(grid[0])
    
    # Queue for BFS
    queue = deque([(start_row, start_col)])
    
    # Keep track of visited cells and their previous cell
    visited = {(start_row, start_col)}
    previous = {}
    
    # Possible movements: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while queue:
        row, col = queue.popleft()
        
        # If we reached the destination
        if row == end_row and col == end_col:
            # Reconstruct the path
            path = []
            current = (end_row, end_col)
            
            while current != (start_row, start_col):
                path.append(current)
                current = previous[current]
            
            path.append((start_row, start_col))
            path.reverse()
            return path
        
        # Try all four directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)
            
            # Check if the new position is valid
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (grid[new_row][new_col] == 1 or grid[new_row][new_col] == -1) and  # Only roads and cities
                new_pos not in visited):
                
                queue.append(new_pos)
                visited.add(new_pos)
                previous[new_pos] = (row, col)
    
    # No path found
    return None

def find_minimum_spanning_tree(cities, paths):
    """
    Create a minimum spanning tree using Kruskal's algorithm.
    """
    cities_count = len(cities)
    if cities_count <= 1:
        return []
    
    # Create a list of all edges with their weights
    edges = []
    for i in range(cities_count):
        city_key = cities[i]
        
        for j in range(i + 1, cities_count):
            target_key = cities[j]
            
            if city_key in paths and target_key in paths[city_key]:
                # Weight is the length of the path (number of cells)
                weight = len(paths[city_key][target_key])
                edges.append((weight, i, j, paths[city_key][target_key]))
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize MST
    mst = []
    parent = [-1] * cities_count
    
    # Find set function for Union-Find
    def find_set(i):
        if parent[i] == -1:
            return i
        
        # Path compression
        parent[i] = find_set(parent[i])
        return parent[i]
    
    # Union function for Union-Find
    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False
    
    # Kruskal's algorithm
    for weight, u, v, path in edges:
        if union(u, v):
            mst.append(path)
    
    return mst

# Example usage
def print_grid(grid):
    """
    Helper function to print the grid in a readable format.
    """
    for row in grid:
        print(" | ".join(map(str, row)))

# Test with the provided example
if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1, -1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, -1, 0, -1, 1, -1],
        [0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 1]
    ]
    
    print("Input grid:")
    print_grid(grid)
    
    solution = find_minimum_electricity_network(grid)
    
    print("\nOutput grid (electricity network):")
    print_grid(solution)
    
    # Return solution as list of coordinates
    def solution_to_coordinates(grid):
        coords = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 or grid[i][j] == -1:
                    coords.append((i, j))
        return coords
    
    coordinates = solution_to_coordinates(solution)
    print("\nCoordinates of electricity network:", coordinates)