# you are given an array of houses in a neighboorhood in a city.
# you have to rearrange houses in such a way that in a single neighbourhood the houses are sorted by number in ascending order and no 2 houses with same number are in same neighbourhood.
# you can only rearrange house based on the capacity of each neighbourhood . If neighbourhood "1" in input has 2 houses then at output also it can only have 2 houses.


# For example-
# {
# {1,2},
# {4,4,7,8},
# {4,9,9,9}
# }


# becomes
# {
# {4,9},
# {1,2,4,9},
# {4,7,8,9}
# }


# can someone suggest what should be the optimal solution for this.
# Thanks in advance.


# My Solution was :
# 1)Use a hashmap in java to get the frequency count of each house number.
# 2)use a priorityqueue to store the houses
# -based on there frequency
# -if frequency is same then smaller number house should be placed before
# In above example 4 number house has 3 frequency and 9 number house also has 3 frequency
# so we will first pick 4 and allocate it to all the neighbourhood then do the same for others.
# At the end sort the neighbourhood array once again.
# I faced rejection in the interview .
# I was able to code the entire solution .
# I was given 35 minutes for this question .
# Can someone think of another approach ?

# google
from collections import defaultdict
import heapq

def rearrange_houses(neighborhoods):
    # Step 1: Count frequencies of each house number
    freq = defaultdict(int)
    for neighborhood in neighborhoods:
        for house in neighborhood:
            freq[house] += 1
    print(freq)
    
    # Step 2: Create a max heap based on frequencies (negative for max heap)
    max_heap = [(-count, house) for house, count in freq.items()]
    heapq.heapify(max_heap)
    
    # Step 3: Distribute houses to neighborhoods
    result = [[] for _ in neighborhoods]
    capacities = [len(neighborhood) for neighborhood in neighborhoods]
    
    while max_heap:
        count, house = heapq.heappop(max_heap)
        print(count, house)
        count = -count
        
        for i in range(len(neighborhoods)):
            if capacities[i] > 0:
                result[i].append(house)
                capacities[i] -= 1
                count -= 1
                if count == 0:
                    break
        
        if count > 0:
            heapq.heappush(max_heap, (-count, house))
            print("X", (-count, house))
    print(result)
    
    # Step 4: Sort each neighborhood
    for neighborhood in result:
        neighborhood.sort()
    
    return result

# Example usage
neighborhoods = [
    [1, 2],
    [4, 4, 7, 8],
    [4, 9, 9, 9]
]

print(rearrange_houses(neighborhoods))
# Output: [[4, 9], [1, 2, 4, 9], [4, 7, 8, 9]]