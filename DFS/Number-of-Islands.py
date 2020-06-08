"""
Given a 2d grid map of '1's (land) and '0's (water), count the 
number of islands. An island is surrounded by water and is formed 
by connecting adjacent lands horizontally or vertically. You may 
assume all four edges of the grid are all surrounded by water.
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = 'visited'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)

    def main():
        print(numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
                          ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
        print(numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                          ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
        print(numIslands([]))
        print("The values above should be 1, 3, and 0.")
