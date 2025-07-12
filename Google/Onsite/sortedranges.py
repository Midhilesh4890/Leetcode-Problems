from sortedcontainers import SortedList

class Intervals:
    def __init__(self):
        # SortedList to maintain sorted order of interval endpoints
        self.intervals = SortedList()

    def insert(self, start, end):
        # Ensure intervals are inclusive: [start, end]
        # Remove the end += 1 to keep intervals as closed.
        
        # Find the leftmost and rightmost points to adjust intervals
        left_idx = self.intervals.bisect_left(start)
        right_idx = self.intervals.bisect_right(end)

        # Efficiently remove all intervals between left_idx and right_idx
        del self.intervals[left_idx:right_idx]

        # Insert new interval boundaries if they don't overlap
        # Check parity to decide if we need to add start or end
        if left_idx % 2 == 0:
            self.intervals.add(start)
        if right_idx % 2 == 0:
            self.intervals.add(end)

    def query(self, point):
        # Find the insertion point of the query point
        idx = self.intervals.bisect_left(point)

        # Point is inside an interval if idx is odd
        # idx % 2 == 1 means point lies within an interval
        return idx % 2 == 1
obj = Intervals()
obj.insert(1, 5)
obj.insert(10, 15)
print(obj.query(3))   # True (inside [1, 5])
print(obj.query(6))   # False (gap between intervals)
obj.insert(5, 10)
print(obj.query(6))   # True (after merging [1, 15])
