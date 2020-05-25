"""
A robot is located at the top-left corner of a m x n grid (marked 
'Start' in the diagram below). The robot can only move either 
down or right at any point in time. The robot is trying to 
reach the bottom-right corner of the grid (marked 'Finish' 
in the diagram below). Now consider if some obstacles are 
added to the grids. How many unique paths would there be?
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        if obstacleGrid[n-1][m-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        ways = [[1] * m] * n
        for i in range(0, n):
            for j in range(0, m):
                if obstacleGrid[i][j] == 1 and i == 0:
                    k = j
                    while k < m:
                        ways[i][k] = 0
                        k += 1
                elif obstacleGrid[i][j] == 1 and j == 0:
                    k = i
                    while k < n:
                        ways[k][j] = 0
                        k += 1
                elif obstacleGrid[i][j] == 1:
                    ways[i][j] = 0
                elif obstacleGrid[i][j] == 0 and i > 0 and j > 0:
                    ways[i][j] = ways[i-1][j] + ways[i][j-1]
        return ways[n-1][m-1]


# Another way to solve it with reduced space complexity:
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        length = len(obstacleGrid[0])
        dp = [0] * length
        dp[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(length):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[length - 1]


print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(uniquePathsWithObstacles([[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
print(uniquePathsWithObstacles([[1, 0], [0, 0]]))
print("The values above should be 2, 0, and 0.")
