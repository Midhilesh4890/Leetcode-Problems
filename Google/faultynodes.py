# Round 1 (45 Mins):


# Given an undirected graph with some faulty nodes where you are not allowed to visit. Is it possible to reach from node A to node B?


# Follow up: If we consider the cost to be 1 of each teleportation what’s the minimum cost?
# Follow up: if we can repair the node by paying amount C (C can be different for each faulty node). What's the minimum cost now?
# Follow up: if we can repair the node by paying amount C (same cost for all faulty nondes.). and all other nodes are free to travel, what's the cost now?
from collections import deque, defaultdict
from heapq import *

def can_reach(graph, faulty_nodes, A, B):
    if A in faulty_nodes or B in faulty_nodes:
        return False  
    visited = set()
    queue = deque([A])
    visited.add(A)
    
    while queue:
        current = queue.popleft()
        if current == B:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in faulty_nodes:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False
if __name__ == "__main__":
    graph = defaultdict(list)
    edges = [
        ('A', 'x'),
        ('x', 'y'),
        ('y', 'D'),
        ('B', 'y'),
    ]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  
    
    faulty_nodes = {'z'}  
    A = 'A'
    B = 'D'
    
    min_steps = min_teleportations(graph, faulty_nodes, A, B)
    print("Minimum Teleportations:", min_steps)

#Follow up: If we consider the cost to be 1 of each teleportation what’s the minimum cost?
def min_teleportations(graph, faulty_nodes, A, B):

    if A in faulty_nodes or B in faulty_nodes:
        return -1  
    
    visited = set()
    queue = deque([(A, 0)])  
    visited.add(A)
    
    while queue:
        current, distance = queue.popleft()
        if current == B:
            return distance
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in faulty_nodes:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1  
    
# Follow up: if we can repair the node by paying amount C (C can be different for each faulty node). What's the minimum cost now?

def min_total_cost_varying(graph, faulty_nodes, repair_costs, A, B):

    
    heap = []
    heappush(heap, (0, A))
    

    min_cost = {}
    min_cost[A] = 0
    
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        
        if current_node == B:
            return current_cost
        

        for neighbor in graph[current_node]:
            if neighbor in faulty_nodes:
                repair_cost = repair_costs.get(neighbor, float('inf'))
                new_cost = current_cost + 1 + repair_cost  
               
                if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))
            else:
                new_cost = current_cost + 1
                if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))
    
    return -1  

# Follow up: if we can repair the node by paying amount C (same cost for all faulty nondes.). and all other nodes are free to travel, what's the cost now?
def min_total_cost_uniform(graph, faulty_nodes, C, A, B):

    heapq.heappush(heap, (0, A))
    
    min_cost = {}
    min_cost[A] = 0
    
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        
        if current_node == B:
            return current_cost
        
       for neighbor in graph[current_node]:
            if neighbor in faulty_nodes:
                new_cost = current_cost + 1 + C  # 1 for teleportation + C for repair
                
                if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))
            else:
                 new_cost = current_cost + 1
                if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))
    
    return -1 