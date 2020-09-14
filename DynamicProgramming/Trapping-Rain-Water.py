"""
Given n non-negative integers representing an elevation map where the width 
of each bar is 1, compute how much water it is able to trap after raining.
"""


class Solution:
    def trap(self, height: List[int]):
        if not height:
            return 0
        total, n = 0, len(height)
        left, right = [0] * n, [0] * n
        for i in range(0, n):
            left[i] = max(left[i - 1], height[i])
        right[n-1] = height[n-1]
        for j in range(n - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])
        for k in range(n):
            total += min(left[k], right[k]) - height[k]
        return total


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap([0, 3, 0, 4, 2, 0, 1, 3, 2]))
print(trap([0, 4, 0, 4, 4, 0, 4, 4]))
print("The values above should be 6, 9, and 8.")
