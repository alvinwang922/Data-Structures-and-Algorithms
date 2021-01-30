"""
Given an m x n matrix of non-negative integers representing the height of each unit cell 
in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the 
"Atlantic ocean" touches the right and bottom edges. Water can only flow in four directions 
(up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
"""


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        pacific = set()
        atlantic = set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[next_i][next_j] >= matrix[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, pacific)
            traverse(row, cols - 1, atlantic)

        for col in range(cols):
            traverse(0, col, pacific)
            traverse(rows - 1, col, atlantic)

        return list(pacific & atlantic)

    print(pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
        2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
    print("The solution above should be [[4, 0], [0, 4], [3, 1], \
        [1, 4], [3, 0], [2, 2], [1, 3]].")
