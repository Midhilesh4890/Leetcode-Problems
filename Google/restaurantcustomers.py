# I had Google phone screening round recently. Below is the question asked


# Design a data structure for restaurant customers waitlsit which should support
# a. New customer groups can be added to waitlist
# b. A waiting customer group can leave at any time
# c. Given a tableSize, you need to find the right customer group which can be assigned to the input table. A group is eligible for a table if it's size is <= tableSize and among those groups you need to select the one who has arrived first.


# For example -


# Current waitlist - [4,2,3,6] - In order of their arrival, each element indicates the size of the group
# Customer group of size 5 enters the waitlist then updated waitlist would be - [4,2,3,6,5]
# 4th group(index 3) leaves the waitlist. Updated wailist - [4,2,3,5]
# findGroup for table size 3. output - group 2(index 1)
# eligible groups - 2(index 1),3(index 2) for tablesize 3 but since group of size 2 has arrived before group of size 3, return group of size
# Help me with the most optimal solution.


from sortedcontainers import SortedDict
from collections import OrderedDict

class RestaurantWaitlist:
    def __init__(self):
        self.waitlist = OrderedDict()  # Maintains order of arrival
        self.size_map = SortedDict()   # Maps size -> list of indices (Sorted by size)
        self.index_map = {}  # Maps customer ID to their node (for quick deletion)
        self.counter = 0      # Unique identifier for customer groups

    def add_customer_group(self, size: int):
        """Adds a new customer group to the waitlist"""
        self.waitlist[self.counter] = size
        if size not in self.size_map:
            self.size_map[size] = set()
        self.size_map[size].add(self.counter)
        self.index_map[self.counter] = size
        self.counter += 1  # Increment for unique group ID

    def remove_customer_group(self, group_id: int):
        """Removes a specific customer group by its ID"""
        if group_id in self.index_map:
            size = self.index_map[group_id]
            del self.waitlist[group_id]  # Remove from ordered dict
            self.size_map[size].remove(group_id)  # Remove from size mapping
            if not self.size_map[size]:  # Clean up empty sizes
                del self.size_map[size]
            del self.index_map[group_id]

    def find_group_for_table(self, table_size: int):
        """Finds the first eligible customer group for the given table size"""
        for size in self.size_map.irange(maximum=table_size):
            if self.size_map[size]:  # Find first valid group
                first_group_id = min(self.size_map[size])  # Get the earliest added group
                return first_group_id
        return -1  # No suitable group found

    def display_waitlist(self):
        """Displays the current waitlist"""
        print(list(self.waitlist.values()))


# **Example Usage**
waitlist = RestaurantWaitlist()
waitlist.add_customer_group(4)
waitlist.add_customer_group(2)
waitlist.add_customer_group(3)
waitlist.add_customer_group(6)
waitlist.display_waitlist()  # Output: [4, 2, 3, 6]

waitlist.add_customer_group(5)
waitlist.display_waitlist()  # Output: [4, 2, 3, 6, 5]

waitlist.remove_customer_group(3)  # Remove group at index 3 (6)
waitlist.display_waitlist()  # Output: [4, 2, 3, 5]

print(waitlist.find_group_for_table(3))  # Output: 1 (Group of size 2)
