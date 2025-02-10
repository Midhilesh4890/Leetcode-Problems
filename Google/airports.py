from collections import defaultdict
import heapq

from collections import defaultdict
import heapq

def can_reach_destination(airport, destination, flights):
    # Create a graph representation where each airport maps to a list of outgoing flights
    graph = defaultdict(list)
    for dep, arr, dep_time, arr_time in flights:
        graph[dep].append((arr, dep_time, arr_time))
    
    # Min heap (priority queue) to track the earliest time we can reach an airport
    # Each element in heap is (arrival_time, airport)
    min_heap = [(0, airport)]  # We start at the airport with time 0
    arrival_times = {airport: 0}  # Dictionary to keep track of the earliest arrival times
    
    while min_heap:
        curr_time, airport = heapq.heappop(min_heap)  # Get the airport with the earliest arrival time
        
        # If we have reached the destination, return True
        if airport == destination:
            return True
        
        # Process all flights departing from the current airport
        for next_airport, dep_time, arr_time in graph[airport]:
            # The package can only board the flight if it has already arrived at the airport before departure
            if curr_time <= dep_time:  # Ensure the transfer condition is met
                # If the next airport has not been visited OR we found a quicker way to reach it
                if next_airport not in arrival_times or arr_time < arrival_times[next_airport]:
                    arrival_times[next_airport] = arr_time  # Update the earliest arrival time
                    heapq.heappush(min_heap, (arr_time, next_airport))  # Push to the heap for further exploration
    
    # If we exit the loop without reaching the destination, return False
    return False

# Example test cases
flights1 = [("NYC", "LAX", 0, 4), ("LAX", "SFO", 5, 7)]
print(can_reach_destination("NYC", "SFO", flights1))  # Output: True

flights2 = [("NYC", "LAX", 0, 4), ("LAX", "SFO", 3, 5)]
print(can_reach_destination("NYC", "SFO", flights2))  # Output: False

