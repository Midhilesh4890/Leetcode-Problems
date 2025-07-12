class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

def find_similar_videos_dsu(videos, i):
    # Build a tag to video mapping
    tag_to_videos = {}
    for j in range(i):
        for tag in videos[j]:
            if tag not in tag_to_videos:
                tag_to_videos[tag] = []
            tag_to_videos[tag].append(j)
    
    # Initialize DSU for videos up to i-1
    uf = UnionFind(i)
    
    # Union videos that share tags
    for tag, video_list in tag_to_videos.items():
        for j in range(1, len(video_list)):
            uf.union(video_list[0], video_list[j])
    
    # Find videos that share tags with video i
    similar_videos = set()
    for tag in videos[i]:
        if tag in tag_to_videos:
            for j in tag_to_videos[tag]:
                similar_videos.add(j)
    
    return sorted(list(similar_videos))

# Test cases
test_case_1 = [
    {"action", "comedy"},           # Video 0
    {"drama", "thriller"},          # Video 1
    {"comedy", "romance"},          # Video 2
    {"action", "sci-fi"},           # Video 3
    {"horror", "thriller"},         # Video 4
]

print("Test Case 1:")
print(f"DSU approach: {find_similar_videos_dsu(test_case_1, 3)}")
# Expected: [0]
print(f"DSU approach: {find_similar_videos_dsu(test_case_1, 4)}")
# Expected: [1]

test_case_2 = [
    {"python", "coding", "algorithm"},    # Video 0
    {"java", "coding", "oop"},            # Video 1
    {"c++", "algorithm", "performance"},  # Video 2
    {"javascript", "web", "frontend"},    # Video 3
    {"python", "web", "backend"},         # Video 4
]

print("\nTest Case 2:")
print(f"DSU approach: {find_similar_videos_dsu(test_case_2, 4)}")
# Expected: [0, 3]