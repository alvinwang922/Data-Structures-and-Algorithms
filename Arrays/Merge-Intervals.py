"""
Given a collection of intervals, merge all overlapping intervals.
"""


def merge(intervals: List[List[int]]) -> List[List[int]]:
    final = []
    for i in sorted(intervals):
        if final and i[0] <= final[-1][1]:
            final[-1][1] = max(final[-1][1], i[1])
        else:
            final += i,
    return final


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))
print(merge([]))
print("The arrays above should be [[1, 6], [8, 10], [15, 18]], \
    [[1, 5]], and [].")
