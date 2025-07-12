def longest_loss_period(prices):
    min_price = float('inf')  # Track the minimum price seen so far
    min_time = None  # Track the time when min_price occurred
    longest_duration = 0  # Store the longest period of loss
    
    for time, price in prices:
        if price < min_price:
            min_price = price
            min_time = time  # Update minimum price time
        
        if price > min_price:  # Loss period ends
            longest_duration = max(longest_duration, time - min_time)
    
    return longest_duration

# Sample input
prices = [
    (100, 5), 
    (200, 6), 
    (300, 2), 
    (400, 5), 
    (500, 5), 
    (600, 7)
]

print(longest_loss_period(prices))  # Output: 300
