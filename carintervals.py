# Given stream of time interval tell that min how many cars will be used to book for all timeintervals;


# Given : {{1,3}, {2,5},{6,8},{7,10},{9,10}}
# output :
# car1 : {1,3},{6,8},{9,10}
# car2 : {2,5},{7,10}

LAST_HOUR = 2400  # Time limit assumption (24-hour format)

def minCars_prefix_sum(intervals):
    occupancy = [0] * LAST_HOUR  # Initialize array to track occupancy
    
    # Step 1: Mark arrivals and departures
    for start, end in intervals:
        occupancy[start] += 1  # A car is booked
        occupancy[end] -= 1  # A car is released
    
    # Step 2: Compute prefix sum to track concurrent bookings
    max_cars = 0
    current_cars = 0
    for i in range(LAST_HOUR):
        current_cars += occupancy[i]
        max_cars = max(max_cars, current_cars)  # Track peak usage

    return max_cars

# Example usage:
intervals = [[1, 3], [2, 5], [6, 8], [7, 10], [9, 10]]
print(minCars_prefix_sum(intervals))  # Output: 2

def minCars_event_based(intervals):
    events = []
    
    # Step 1: Convert intervals into start and end events
    for start, end in intervals:
        events.append((start, 1))  # Booking starts
        events.append((end, -1))   # Booking ends
    
    # Step 2: Sort events
    events.sort()  # Sorting ensures processing in chronological order
    
    max_cars = 0
    current_cars = 0

    # Step 3: Process events in order
    for _, event in events:
        current_cars += event  # Increase or decrease car count
        max_cars = max(max_cars, current_cars)  # Track max concurrent usage

    return max_cars

# Example usage:
intervals = [[1, 3], [2, 5], [6, 8], [7, 10], [9, 10]]
print(minCars_event_based(intervals))  # Output: 2
