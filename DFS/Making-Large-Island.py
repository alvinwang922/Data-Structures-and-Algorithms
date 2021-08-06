"""
You are given an n x n binary matrix grid. You are allowed to 
change at most one 0 to be 1. Return the size of the largest 
island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.
"""

from collections import defaultdict


def largestIsland(grid: List[List[int]]):
    x, y = len(grid[0]), len(grid)
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    counter = defaultdict(int)
    curr, ans = 2, 0

    def dfs(num, i, j):
        if not 0 <= i < y or not 0 <= j < x or grid[i][j] != 1:
            return
        counter[num] += 1
        grid[i][j] = num
        for a, b in directions:
            dfs(num, i+a, j+b)

    for x_i in range(x):
        for y_i in range(y):
            if grid[y_i][x_i] == 1:
                dfs(curr, y_i, x_i)
                curr += 1

    for x_i in range(x):
        for y_i in range(y):
            if grid[y_i][x_i] == 0:
                islands = set()
                for dx, dy in directions:
                    if 0 <= x_i + dx < x and 0 <= y_i + dy < y and grid[y_i+dy][x_i+dx] != 0:
                        islands.add(grid[y_i+dy][x_i+dx])
                ans = max(ans, sum(counter[i] for i in islands) + 1)
    if ans:
        return ans
    return x * y


print(largestIsland([[1, 0], [0, 1]]))
print(largestIsland([[1, 1], [1, 0]]))
print("The values above should be 3 and 4.")
