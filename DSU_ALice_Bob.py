# This was my last coding interview of the onsite process. Here's the question


# Write a function that takes the following 3 queries:


#     1. manager, a, b      -> represents that a is manager of b
#     2. peer, a, b         -> both a and b have the same manager
#     3. is_manager a, b    -> you should return whether a is manager of b
# Assume every input is valid.
# Assume every query is coming one at a time, not a list of queries.
# Interviewer said I might come across a case where a peer query came with two managerless employees

class DSU:
    def __init__(self):
        self.parent = {}  # Tracks the immediate parent (manager)
        self.rank = {}  # Rank for union by rank
        self.actual_manager = {}  # Tracks the highest manager of an employee

    def find(self, x):
        """Finds the root manager of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, a, b):
        """Union two employees under the same manager."""
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA != rootB:
            # Union by rank heuristic
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1

    def set_manager(self, manager, employee):
        """Sets `manager` as the manager of `employee`."""
        if manager not in self.parent:
            self.parent[manager] = manager  # Manager manages itself
            self.rank[manager] = 0
        if employee not in self.parent:
            self.parent[employee] = employee
            self.rank[employee] = 0
        
        # Set manager-employee relationship
        self.parent[employee] = manager

    def add_peer(self, a, b):
        """Makes `a` and `b` peers (same manager)."""
        if a not in self.parent:
            self.parent[a] = a  # Default to self if no manager
            self.rank[a] = 0
        if b not in self.parent:
            self.parent[b] = b
            self.rank[b] = 0

        # Merge their sets to make them peers
        self.union(a, b)

    def is_manager(self, a, b):
        """Checks if `a` is a manager of `b`."""
        if a not in self.parent or b not in self.parent:
            return False
        return self.find(b) == a  # Check if `a` is an ancestor of `b`

# Example usage
dsu = DSU()
dsu.set_manager("Alice", "Bob")
dsu.set_manager("Alice", "Charlie")
dsu.add_peer("Bob", "Charlie")  # Bob and Charlie should have the same manager
print(dsu.is_manager("Alice", "Bob"))  # True
print(dsu.is_manager("Bob", "Charlie"))  # False
