"""
Given an integer matrix, find the length of the longest 
increasing path. From each cell, you can either move to 
four directions: left, right, up or down. You may NOT 
move diagonally or move outside of the boundary (i.e. 
wrap-around is not allowed).
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]):
        if not matrix:
            return 0
        dp = [[0 for i in range(len(matrix[0]))]
              for j in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.dfs(matrix, i, j, dp, -1))
        return ans

    def dfs(self, matrix, i, j, dp, prev):
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ans = 0
        if i < 0 or i >= len(matrix) or j < 0 or \
                j >= len(matrix[0]) or matrix[i][j] <= prev:
            return 0
        if dp[i][j]:
            return dp[i][j]
        for a, b in directions:
            ans = max(ans, self.dfs(matrix, i + a,
                                    j + b, dp, matrix[i][j]))
        ans += 1
        dp[i][j] = ans
        return ans

    print(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    print(longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 7]]))
    print(longestIncreasingPath([[1, 2]]))
    print("The values above should be 4 and 5, and 2.")
