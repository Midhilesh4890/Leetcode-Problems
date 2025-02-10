# # import bisect

# # def solve(input, sorted_stream, target):
# #     # Insert element while maintaining sorted order
# #     bisect.insort(sorted_stream, input)

# #     # Check the entire sorted stream for any triplet that meets the simplified distance condition
# #     i = 0
# #     while i < len(sorted_stream) - 2:
# #         # Extract the potential triplet
# #         a, c = sorted_stream[i], sorted_stream[i + 2]
        
# #         # Check if the distance between the first and last in the triplet is less than target
# #         if abs(a - c) < target:
# #             # Triplet found that meets the condition
# #             triplet = sorted_stream[i:i+3]
# #             print("Triplet found:", triplet)

# #             # Remove these elements from the sorted stream
# #             del sorted_stream[i:i+3]
# #             # Continue checking from the current index as the list has been modified
# #             continue
        
# #         i += 1

# # # Main program loop
# # sorted_stream = []
# # target_distance = 3

# # while True:
# #     try:
# #         # Accept input from the user
# #         data = input("Enter a floating-point number (or type 'exit' to quit): ")
# #         if data.lower() == 'exit':
# #             break
# #         data = float(data)
# #         solve(data, sorted_stream, target_distance)
# #         print("Current stream state:", sorted_stream)
# #     except ValueError:
# #         print("Please enter a valid floating-point number or 'exit'.")

# # # Output the remaining elements in the stream after processing
# # print("Remaining elements in the stream after exit:", sorted_stream)



# # class UnionFind:
# #     def __init__(self, ids):
# #         self.parent = {id: id for id in ids}
# #         self.rank = {id: 0 for id in ids}

# #     def find(self, id):
# #         if self.parent[id] != id:
# #             self.parent[id] = self.find(self.parent[id])  # Path compression
# #         return self.parent[id]

# #     def union(self, id1, id2):
# #         root1 = self.find(id1)
# #         root2 = self.find(id2)

# #         if root1 != root2:  # Union by rank
# #             if self.rank[root1] > self.rank[root2]:
# #                 self.parent[root2] = root1
# #             elif self.rank[root1] < self.rank[root2]:
# #                 self.parent[root1] = root2
# #             else:
# #                 self.parent[root2] = root1
# #                 self.rank[root1] += 1

# # def group_objects(objects):
# #     uf = UnionFind([obj['id'] for obj in objects])
# #     property_map = {}

# #     for obj in objects:
# #         properties = (obj['p1'], obj['p2'], obj['p3'])
# #         for prop in properties:
# #             if prop in property_map:
# #                 uf.union(property_map[prop], obj['id'])
# #             property_map[prop] = obj['id']  # Associate this property with current id

# #     # Group ids by their root id
# #     groups = {}
# #     for obj_id in uf.parent:
# #         root_id = uf.find(obj_id)
# #         if root_id not in groups:
# #             groups[root_id] = []
# #         groups[root_id].append(obj_id)

# #     return list(groups.values())

# # # Example usage
# # objects = [
# #     {'id': 'id1', 'p1': 'p1', 'p2': 'p2', 'p3': 'p3'},
# #     {'id': 'id2', 'p1': 'p1', 'p2': 'p4', 'p3': 'p5'},
# #     {'id': 'id3', 'p1': 'p6', 'p2': 'p7', 'p3': 'p8'},
# #     {'id': 'id4', 'p1': 'p9', 'p2': 'p10', 'p3': 'p5'}
# # ]

# # grouped_ids = group_objects(objects)
# # print(grouped_ids)  # Output: [['id1', 'id2', 'id4'], ['id3']]

# # import heapq

# # def dijkstra(graph, start):
# #     # Distance dictionary to store the minimum distance to each node
# #     distances = {node: float('inf') for node in graph}
# #     distances[start] = 0
# #     # Priority queue to store vertices to be examined with their current shortest distances
# #     priority_queue = [(0, start)]
    
# #     while priority_queue:
# #         current_distance, current_node = heapq.heappop(priority_queue)
        
# #         # Nodes can only be added once to the queue
# #         if current_distance > distances[current_node]:
# #             continue
        
# #         for neighbor, weight in graph[current_node].items():
# #             distance = current_distance + weight
            
# #             # Only consider this new path if it's better
# #             if distance < distances[neighbor]:
# #                 distances[neighbor] = distance
# #                 heapq.heappush(priority_queue, (distance, neighbor))
    
# #     return distances

# # def nearest_favorite_city(graph, start, favorite_cities):
# #     distances = dijkstra(graph, start)
# #     nearest_city = None
# #     min_distance = float('inf')
    
# #     for city in favorite_cities:
# #         if city in distances and distances[city] < min_distance:
# #             nearest_city = city
# #             min_distance = distances[city]
    
# #     return nearest_city, min_distance

# # # Example graph (Adjacency list representation)
# # graph = {
# #     'A': {'B': 5, 'C': 1},
# #     'B': {'A': 5, 'C': 2, 'D': 1},
# #     'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
# #     'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
# #     'E': {'C': 8, 'D': 3},
# #     'F': {'D': 6}
# # }

# # favorite_cities = ['E', 'F']
# # start = 'A'

# # nearest_city, distance = nearest_favorite_city(graph, start, favorite_cities)
# # print(f"The nearest favorite city from {start} is {nearest_city} with a distance of {distance}")
# # For each element, if it's greater than or equal to the maximum value from the left (max_left[i]) 
# # and less than or equal to the minimum value from the right (min_right), it is counted as binary searchable.

# from itertools import accumulate
# def binary_searchable(nums):
#     n = len(nums)
#     count = 0

#     # Array to store the maximum values seen from the left up to each index
#     max_left = list(accumulate(nums, max))
#     print(max_left)

#     # Variable to track the minimum value seen from the right starting from each index
#     min_right = float('inf')
#     for i in range(n - 1, -1, -1):
#         min_right = min(min_right, nums[i])
#         # Check if the current element is greater than or equal to the max on its left
#         # and less than or equal to the min on its right
#         if nums[i] <= min_right and nums[i] >= max_left[i]:
#             count += 1

#     return count

# # Example usage
# nums = [2, 1, 3, 4, 5, 6]
# print(binary_searchable(nums))  # Output the count of binary searchable elements


# import pandas as pd

# data = {
#     'CustomerID': [1, 2, 3, 4, 5],
#     'Age': [30, 45, 25, 35, 50],
#     'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
#     'Tenure': [12, 24, 6, 18, 36],
#     'ContractType': ['Month-to-Month', 'One year', 'Month-to-Month', 'Two year', 'One year'],
#     'MonthlyCharges': [50, 60, 45, 70, 80],
#     'Churn': [0, 1, 0, 0, 1]
# }

# df = pd.DataFrame(data)

# # Questions:
# # 1. Calculate the churn rate for each contract type.

# churn_rate = df.group_by('ContractType')['Churn'].mean().reset_index(name = 'Churn')


# Decompress Strings
# "3[b]2[bc]" -> "bbbbcbc"
# "3[x2[c]]" -> "xccxccxcc"
# "2[ab]3[cd]hf" -> ababcdcdcdhf"

# step1 : ']'

# stack = [(value , string)]

# pop the stack 

# res = ''

def solve(s):

    res = ''
    val = 0
    stack = [] # (val, res)

    for i in s:
        if i.isdigit(): val = 10 * val + int(i)
        elif i == ']': res = stack.pop() + stack.pop() * res
        elif i == '[':
            stack.extend([val, res])
            val = 0
            res = ''
        else:
            res += i 
    return res 
s = '3[x2[c[2][c][c[c[c[c[c]]]]]]]'
print(solve(s))







