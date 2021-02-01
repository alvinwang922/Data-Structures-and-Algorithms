"""
Given a matrix of integers A with R rows and C columns, find the 
maximum score of a path starting at [0,0] and ending at [R-1,C-1].
The score of a path is the minimum value in that path. For example, 
the value of the path 8 →  4 →  5 →  9 is 4.
A path moves some number of times from one visited cell to any 
neighbouring unvisited cell in one of the 4 cardinal directions 
(north, east, west, south).
"""

from collections import heapq


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]):
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col = len(A), len(A[0])
        maxHeap = [(-A[0][0], 0, 0)]
        visited = [[0 for _ in range(col)] for _ in range(row)]
        while maxHeap:
            curr, x, y = heapq.heappop(maxHeap)
            if x == row - 1 and y == col - 1:
                return -curr
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    heapq.heappush(maxHeap, (max(curr, -A[nx][ny]), nx, ny))
        return -1

    print(maximumMinimumPath([[5, 4, 5], [1, 2, 6], [7, 4, 6]]))
    print(maximumMinimumPath([[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]))
    print(maximumMinimumPath([[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], \
        [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]))
    print("The values above should be 4, 2, and 3.")
