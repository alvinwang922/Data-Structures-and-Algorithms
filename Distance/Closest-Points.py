"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.) You may return the
answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]


print(kClosest([[1, 3], [-2, 2]], 1))
print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))
print(kClosest([[1, 2], 1))
print("The arrays above should be [[-2, 2]], [[3, 3], [-2, 4]], and [[1, 2]].")
