# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

#Solution 1:

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    result = []
    for i in intervals[1:]:
        if i[0] > end:
            result.append([start, end])
            start = i[0]
            end = i[1]
        else:
            end = max(end, i[1])
    result.append([start, end])
    return result

#Solution 2 -- Better code


def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for start,end in intervals[1:]:
        if start > result[-1][1]:
            result.append([start, end])
        else:
            end = max(end, i[1])
    result.append([start, end])
    return result

