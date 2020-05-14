# A robot is located at the top-left corner of a
# m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at
# any point in time. The robot is trying to reach
# the bottom-right corner of the grid (marked
# 'Finish' in the diagram below).
# How many possible unique paths are there?


class Solution(object):
    def uniquePaths(self, m, n):
        ways = [[1] * m] * n
        for i in range(1, n):
            for j in range(1, m):
                ways[i][j] = ways[i-1][j] + ways[i][j-1]
        return ways[n-1][m-1]


print(uniquePaths(3, 2))
print(uniquePaths(7, 3))
print(uniquePaths(7, 4))
print("The values above should be 3, 28, and 84.")
