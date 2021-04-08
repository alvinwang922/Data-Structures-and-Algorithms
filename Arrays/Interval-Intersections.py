"""
Given two lists of closed intervals, each list of intervals is pairwise 
disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real 
numbers x with a <= x <= b.  The intersection of two closed intervals is 
a set of real numbers that is either empty, or can be represented as a 
closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
"""


def intervalIntersection(A: List[List[int]], B: List[List[int]]):
    a, b, intervals = 0, 0, []
    while a < len(A) and b < len(B):
        aInterval = A[a]
        bInterval = B[b]
        start = max(aInterval[0], bInterval[0])
        end = min(aInterval[1], bInterval[1])
        if end >= start:
            intervals.append([start, end])
        if aInterval[1] >= bInterval[1]:
            b += 1
        else:
            a += 1
    return intervals


print(intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                           [[1, 5], [8, 12], [15, 24], [25, 26]]))
print("The intervals above should be [[1, 2], [5, 5], [8, 10], \
    [15, 23], [24, 24], [25, 25]].")
