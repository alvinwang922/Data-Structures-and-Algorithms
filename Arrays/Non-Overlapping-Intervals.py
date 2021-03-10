"""
Given a collection of intervals, find the minimum number of intervals 
you need to remove to make the rest of the intervals non-overlapping.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')
        removed = 0
        for i in sorted(intervals, key=lambda i: i[1]):
            if i[0] >= end:
                end = i[1]
            else:
                removed += 1
        return removed

    print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(eraseOverlapIntervals([[1, 2], [2, 3]]))
    print("The integers above should be 1, 2, and 0.")
