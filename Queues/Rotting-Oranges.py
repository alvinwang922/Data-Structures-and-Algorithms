"""
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent 
(4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse 
until no cell has a fresh orange.  If this is 
impossible, return -1 instead.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        fresh = 0
        rot = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rot.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        ans = 0
        while rot and fresh > 0:
            ans += 1
            for _ in range(len(rot)):
                x, y = rot.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    fresh -= 1
                    grid[xx][yy] = 2
                    rot.append((xx, yy))
        return ans if fresh == 0 else -1


print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(orangesRotting([[0, 2]]))
print("The values above should be 4, -1, and 0.")
