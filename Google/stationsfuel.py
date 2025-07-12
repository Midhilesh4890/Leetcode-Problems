import heapq

def minRefuelStops(distance, tank, stations):
    stations.append((distance, 0))

    # Max heap to store fuel available at stations we passed
    max_heap = []
    
    # Current fuel and previous position initialization
    curr_fuel = tank
    prev_position = 0
    refuel_stops = 0

    for position, fuel in stations:
        # Calculate fuel consumed to reach the next station
        curr_fuel -= (position - prev_position)

        # If at any point we run out of fuel before reaching the next station
        while max_heap and curr_fuel < 0:
            curr_fuel += -heapq.heappop(max_heap)  # Get max fuel available
            refuel_stops += 1

        # If we still don't have enough fuel, return -1 (can't reach destination)
        if curr_fuel < 0:
            return -1

        # Add current station's fuel to the max heap (negative for max heap)
        heapq.heappush(max_heap, -fuel)

        # Update previous position
        prev_position = position

    return refuel_stops

def test():
    # Test Case 1: Basic example
    print(minRefuelStops(100, 10, [(10, 10), (20, 20), (30, 30), (60, 40)]))
test()

distance = 100
tank = 10
stations = [(10, 10), (20, 20), (30, 30), (60, 40)]

print(minRefuelStops(distance, tank, stations))