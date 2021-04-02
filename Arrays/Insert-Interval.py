"""
Given a set of non-overlapping intervals, insert a new interval into the 
intervals (merge if necessary). You may assume that the intervals were 
initially sorted according to their start times.
"""


def insert(self, intervals: List[List[int]], newInterval: List[int]):
    front = []
    back = []
    intervalStart = newInterval[0]
    intervalEnd = newInterval[1]
    for i in intervals:
        if i[1] < newInterval[0]:
            front.append(i)
        elif i[0] > newInterval[1]:
            back.append(i)
        else:
            intervalStart = min(intervalStart, i[0])
            intervalEnd = max(intervalEnd, i[1])
    return front + [[intervalStart, intervalEnd]] + back


print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(insert([[1, 5]], [1, 3]))
print("The arrays above should be [[1, 5], [6, 9]], \
    [[1, 2], [3, 10], [12, 16]], and [[1, 5]]")
