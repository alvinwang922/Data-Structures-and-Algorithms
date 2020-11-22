"""
On a 2D plane, we place stones at some integer coordinate points. 
Each coordinate point may have at most one stone. Now, a move 
consists of removing a stone that shares a column or row with 
another stone on the grid. What is the largest possible number 
of moves we can make?
"""


import collections


class Solution:
    def removeStones(self, stones: List[List[int]]):
        if not stones:
            return 0

        def dfs(rows, columns, unvisited, x, y):
            if (x, y) in unvisited:
                unvisited.remove((x, y))
                for i in rows[x]:
                    dfs(rows, columns, unvisited, x, i)
                for j in columns[y]:
                    dfs(rows, columns, unvisited, j, y)
        rows = collections.defaultdict(list)
        columns = collections.defaultdict(list)
        unvisited = set((stone[0], stone[1]) for stone in stones)
        islands = 0
        for stone in stones:
            rows[stone[0]].append(stone[1])
            columns[stone[1]].append(stone[0])
        for stone in stones:
            if (stone[0], stone[1]) in unvisited:
                dfs(rows, columns, unvisited, stone[0], stone[1])
                islands += 1
        return len(stones) - islands

    print(removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
    print(removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
    print(removeStones([[0, 0]]))
    print("The values above should be 5, 3, and 0.")
