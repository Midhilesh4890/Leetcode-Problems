# You're given a list of elements. Each element has a unique id and 3 properties. Two elements are considered as duplicates if they share any
# of the 3 properties. Please write a function that takes the input and returns all the duplicates.


# Input:
# E1: id1, p1, p2, p3
# E2: id2, p1, p4, p5
# E3: id3, p6, p7, p8


# Output: {{id1, id2}, {id3}}


# Input:
# E1: id1, p1, p2, p3
# E2: id2, p1, p4, p5
# E3: id3, p5, p7, p8


# Output: {{id1, id3, id3}}


# Does anyone know how to solve this?

class UnionFind:
    def __init__(self, n):
        # Initialize the UnionFind structure with `n` elements
        # `parent` stores the parent of each node, initialized to point to itself
        self.parent = list(range(n))
        # `size` stores the size of the set for each root node, initially 1
        self.size = [1] * n

    def find(self, node):
        # Recursive path compression function that finds the root of the given node
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Compress path
        return self.parent[node]

    def union(self, node1, node2):
        # Union by size: Connects roots of two nodes if they are not already connected
        p1, p2 = self.find(node1), self.find(node2)
        if p1 != p2:  # Only union if different sets
            if self.size[p1] < self.size[p2]:  # Attach smaller tree under larger tree
                self.parent[p1] = p2
                self.size[p2] += self.size[p1]  # Update the size of the root
            else:
                self.parent[p2] = p1
                self.size[p1] += self.size[p2]

def findDuplicates(elements):
    n = len(elements)
    uf = UnionFind(n)
    prop_to_index = {}  # Dictionary to map properties to their last seen index

    for i, (id, p1, p2, p3) in enumerate(elements):
        # Loop through each property of the element
        for prop in (p1, p2, p3):
            if prop in prop_to_index:
                # Union current element with the element that last saw this property
                uf.union(prop_to_index[prop], i)
            # Update last seen index for this property
            prop_to_index[prop] = i

    # Dictionary to accumulate ids by the root of their set
    root_to_ids = {}
    for i, (id, _, _, _) in enumerate(elements):
        root = uf.find(i)  # Find the root of the current element
        if root not in root_to_ids:
            root_to_ids[root] = []
        root_to_ids[root].append(id)  # Append id to the list of its root set

    # Collect grouped ids into a list to return
    return list(root_to_ids.values())

# Example usage
elements1 = [("id1", "p1", "p2", "p3"), ("id2", "p1", "p4", "p5"), ("id3", "p6", "p7", "p8")]
elements2 = [("id1", "p1", "p2", "p3"), ("id2", "p1", "p4", "p5"), ("id3", "p5", "p7", "p8")]

print(findDuplicates(elements1))  # Output: [["id1", "id2"], ["id3"]]
print(findDuplicates(elements2))  # Output: [["id1", "id2", "id3"]]
