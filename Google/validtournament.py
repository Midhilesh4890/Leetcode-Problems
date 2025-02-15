from collections import deque

def is_valid(nums):
    length = len(nums)
    
    if length % 2 != 0:
        return False
    
    queue = deque(nums)
    
    while len(queue) > 1:
        size = len(queue)
        
        for _ in range(0, size, 2):
            if len(queue) < 2:
                return False
            
            player1 = queue.popleft()
            player2 = queue.popleft()
            
            if player1 + player2 != size + 1:
                return False
                
            # Append the smaller number back to the queue
            queue.append(min(player1, player2))
    
    return True

# Test the function with an example
result = is_valid([1,8,4,5,2,7,3,6])
print(result)  # Expected: True