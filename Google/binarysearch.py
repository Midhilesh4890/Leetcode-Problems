# There is a fixed size array of integers. And we are given a number S.
# We need to pick a number x from integers (doesn't have to be in the array) 
# and truncate each array integer to largest optimal number such that 
# sum of array after truncations is storage limit S.

def find_optimal_truncation(nums, S):
    get_sum = lambda x: sum(min(num, x) for num in nums)
    
    l, r = 0, max(nums)
    ans = float('-inf')
    
    while l <= r:
        mid = l + r >> 1
        sum_val = get_sum(mid)
        
        if sum_val <= S:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    
    return ans

nums = [20, 50, 50, 400, 1000]
S = 300

print(find_optimal_truncation(nums, S))



