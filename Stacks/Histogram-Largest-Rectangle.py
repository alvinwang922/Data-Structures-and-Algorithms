"""
Given n non-negative integers representing the histogram's
bar height where the width of each bar is 1, find the area 
of largest rectangle in the histogram.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(largestRectangleArea([1, 1, 2, 2, 3, 3]))
print(largestRectangleArea([2, 1]))
print("The values above should be 10, 9, and 2.")
