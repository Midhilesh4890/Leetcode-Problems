# https://leetcode.com/discuss/interview-question/6082922/Google-online-interview-question

# You are given a list of vote power and states


# votesPower = [1,5,7,8,9,10,20]
# states = ["California", "Texas", "Florida", "Indiana", "Alaska", "Ohio", "Hawaii"]


# And you have two candidates C1 and C2, you need to return a List of List of states that we can make in such an order that both candidates receive the same amount of votes.


# Example: [["California", "Texas", "Florida", "Indiana", "Alaska"], ["Ohio", "Hawaii"]]
# The list can have different combinations, you need to return all the lists of combinations.


# What would be the optimal solution for this problem?


def equal_vote_partitions(votesPower, states):
    total_votes = sum(votesPower)
    if total_votes % 2 != 0:
        return []  # If total votes are odd, partitioning isn't possible
    
    target = total_votes // 2
    n = len(votesPower)
    results = set()  # Using set to store unique partitions

    def helper(index, votes, current_states):
        if votes == target:
            # Create a complement state list
            complement_states = [states[i] for i in range(n) if states[i] not in current_states]
            
            # Sort both partitions to ensure uniqueness
            sorted_partition = (tuple(sorted(current_states)), tuple(sorted(complement_states)))
            
            results.add(sorted_partition)
            return
        
        if votes > target or index >= n:
            return
        
        # Include the current state
        current_states.append(states[index])
        helper(index + 1, votes + votesPower[index], current_states)
        current_states.pop()  
        
        # Exclude the current state
        helper(index + 1, votes, current_states)

    helper(0, 0, [])
    
    return [list(map(list, partition)) for partition in results]  # Convert tuples back to lists

# Example usage
votesPower = [1, 5, 7, 8, 9, 10, 20]
states = ["California", "Texas", "Florida", "Indiana", "Alaska", "Ohio", "Hawaii"]
print(equal_vote_partitions(votesPower, states))

print("##############################################################################################")

def equal_vote_partitions(votesPower, states):
    total_votes = sum(votesPower)
    # If the total is odd, equal partitioning is impossible.
    if total_votes % 2 != 0:
        return []
    
    target = total_votes // 2
    n = len(votesPower)
    
    # Precompute a suffix sum to help prune the recursion:
    # suffix[i] is the sum of votesPower[i:]
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + votesPower[i]
    
    results = []
    
    # Our recursive DFS function:
    # i: current index in votesPower/states to consider.
    # current_sum: the sum of votes in the chosen partition so far.
    # chosen: list of indices that have been chosen for candidate 1.
    #
    # **Note:** We force index 0 (say, "California") to be in candidate 1's partition.
    # This prevents generating the mirror image partition.
    def dfs(i, current_sum, chosen):
        # If we reached the target, the remaining states form the second partition.
        if current_sum == target:
            C1 = [states[j] for j in chosen]
            C2 = [states[j] for j in range(n) if j not in chosen]
            results.append([C1, C2])
            return
        
        # If we've exhausted all states or exceeded the target, backtrack.
        if i >= n or current_sum > target:
            return
        
        # Prune if the remaining votes cannot reach the target.
        if suffix[i] + current_sum < target:
            return
        
        # Choose state i (add its vote power to candidate 1)
        dfs(i + 1, current_sum + votesPower[i], chosen + [i])
        # Do not choose state i (thus, state i goes to candidate 2)
        dfs(i + 1, current_sum, chosen)
    
    # To avoid duplicates, we force the first state (index 0) to always be in candidate 1’s partition.
    dfs(1, votesPower[0], [0])
    return results

# Example usage:
votesPower = [1, 5, 7, 8, 9, 10, 20]
states = ["California", "Texas", "Florida", "Indiana", "Alaska", "Ohio", "Hawaii"]

partitions = equal_vote_partitions(votesPower, states)
for part in partitions:
    print(part)


[[['Alaska', 'California', 'Hawaii'], ['Florida', 'Indiana', 'Ohio', 'Texas']], 
[['Hawaii', 'Ohio'], ['Alaska', 'California', 'Florida', 'Indiana', 'Texas']]]

print("##############################################################################################")

from itertools import accumulate
def solve(votesPower, states):
	total = sum(votesPower)
	if total % 2: return []
	n = len(states)
	target = total // 2

	res = []

	suffixsum = list(accumulate(votesPower[::-1]))[::-1]

	def helper(index, current_sum, partition1):
		if current_sum == target:
			C1 = [states[i] for i in partition1]
			C2 = [states[i] for i in range(n) if i not in partition1]
			res.append([C1, C2])
			return 

		if index >= n or current_sum > target: return 

		if suffixsum[index] + current_sum < target: return # prune if the next elements doesn't contribute to target

		helper(index + 1, current_sum + votesPower[index], partition1 + [index]) # store indices in partition
		helper(index + 1, current_sum, partition1)

	helper(1, votesPower[0], [0])

	return res


votesPower = [1, 5, 7, 8, 9, 10, 20]
states = ["California", "Texas", "Florida", "Indiana", "Alaska", "Ohio", "Hawaii"]

partitions = solve(votesPower, states)
for part in partitions:
    print(part)
