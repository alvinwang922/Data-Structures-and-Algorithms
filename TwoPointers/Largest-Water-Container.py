"""
Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a
container, such that the container contains the most water.
"""


class Solution(object):
    def maxArea(self, height):
        most = 0
        x = len(height) - 1
        y = 0
        while x != y:
            if height[x] > height[y]:
                area = height[y] * (x - y)
                y += 1
            else:
                area = height[x] * (x - y)
                x -= 1
            most = max(most, area)
        return most


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([2, 9, 7]))
print(maxArea([1, 2, 3, 4, 5]))
print("The values above should be 49, 4, and 6.")
