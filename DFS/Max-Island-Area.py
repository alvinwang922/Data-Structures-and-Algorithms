"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is 
no island, the maximum area is 0.)
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        maxArea = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j))
        return maxArea

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = 'visited'
        return 1 + self.dfs(grid, i-1, j) + self.dfs(grid, i+1, j) + \
            self.dfs(grid, i, j-1) + self.dfs(grid, i, j+1)

    def main():
        print maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                               [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])
        print maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
        print maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]])
        print("The values above should be 4, 6 and 0.")
