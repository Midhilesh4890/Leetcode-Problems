class UnionFind:
    def __init__(self, ids):
        self.parent = {id: id for id in ids}
        self.rank = {id: 0 for id in ids}

    def find(self, id):
        if self.parent[id] != id:
            self.parent[id] = self.find(self.parent[id])  # Path compression
        return self.parent[id]

    def union(self, id1, id2):
        root1 = self.find(id1)
        root2 = self.find(id2)

        if root1 != root2:  # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def group_objects(objects):
    uf = UnionFind([obj['id'] for obj in objects])
    property_map = {}

    for obj in objects:
        properties = (obj['p1'], obj['p2'], obj['p3'])
        for prop in properties:
            if prop in property_map:
                uf.union(property_map[prop], obj['id'])
            property_map[prop] = obj['id']  # Associate this property with current id

    # Group ids by their root id
    groups = {}
    for obj_id in uf.parent:
        root_id = uf.find(obj_id)
        if root_id not in groups:
            groups[root_id] = []
        groups[root_id].append(obj_id)

    return list(groups.values())

# Example usage
objects = [
    {'id': 'id1', 'p1': 'p1', 'p2': 'p2', 'p3': 'p3'},
    {'id': 'id2', 'p1': 'p1', 'p2': 'p4', 'p3': 'p5'},
    {'id': 'id3', 'p1': 'p6', 'p2': 'p7', 'p3': 'p8'},
    {'id': 'id4', 'p1': 'p9', 'p2': 'p10', 'p3': 'p5'}
]

grouped_ids = group_objects(objects)
print(grouped_ids)  # Output: [['id1', 'id2', 'id4'], ['id3']]