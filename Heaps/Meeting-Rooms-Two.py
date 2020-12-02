"""
Given an array of meeting time intervals consisting of 
start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.
"""


import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]):
        intervals.sort(key=lambda x: x[0])
        heap = []
        for interval in intervals:
            if heap and heap[0] <= interval[0]:
                heapq.heapreplace(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)

    print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(minMeetingRooms([[7, 10], [2, 4]]))
    print(minMeetingRooms([[0, 1], [0, 2], [0, 3], [0, 4]]))
    print("The values above should be 2, 1, and 4.")
