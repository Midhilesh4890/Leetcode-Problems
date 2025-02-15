from bisect import bisect_left
from collections import defaultdict

class FenwickTree:
    """Binary Indexed Tree (Fenwick Tree) for range sum queries."""
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, delta):
        """Increment index by delta."""
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        """Returns sum from 1 to idx."""
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total

    def range_query(self, left, right):
        """Returns sum in range [left, right]."""
        return self.query(right) - self.query(left - 1)

def count_servers(SERVERS, REQUESTS):
    # Step 1: Sort servers by x_s
    SERVERS.sort()

    # Step 2: Sort requests by x_r
    sorted_requests = sorted(enumerate(REQUESTS), key=lambda x: x[1][0])
    
    # Step 3: Coordinate Compression of y-values
    y_values = sorted(set(y for _, y in SERVERS))
    y_compressed = {val: i+1 for i, val in enumerate(y_values)}  # Map y-values to 1-based indices

    # Step 4: Fenwick Tree for y-values
    bit = FenwickTree(len(y_values))
    
    # Step 5: Process requests in sorted order
    results = [0] * len(REQUESTS)
    server_idx = 0  # Pointer for servers
    
    for req_idx, (x_r, y_r) in sorted_requests:
        # Add servers whose x_s >= x_r into BIT
        while server_idx < len(SERVERS) and SERVERS[server_idx][0] < x_r:
            y_s = SERVERS[server_idx][1]
            bit.update(y_compressed[y_s], 1)  # Add this y to BIT
            server_idx += 1

        # Query BIT for servers where y_s >= y_r
        y_r_idx = bisect_left(y_values, y_r) + 1  # Get compressed index
        results[req_idx] = bit.range_query(y_r_idx, len(y_values))

    return results

# Example Usage
SERVERS = [[1,3], [4,1], [6,6]]
REQUESTS = [[3,2], [1,1], [7,7]]
print(count_servers(SERVERS, REQUESTS))  # Output: [1, 3, 0]
