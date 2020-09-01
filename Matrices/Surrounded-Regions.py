"""
Given a 2D board containing 'X' and 'O' (the letter O), 
capture all regions surrounded by 'X'. A region is captured 
by flipping all 'O's into 'X's in that surrounded region.
"""


class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        queue = collections.deque([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]) \
                        and board[i][j] == "O":
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            if 0 <= i < len(board) and 0 <= j < len(board[0]) \
                    and board[i][j] == "O":
                board[i][j] = "A"
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"


print(solve([["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
print("The matrix above should be [[\"X\",\"X\",\"X\",\"X\"],\
    [\"X\",\"X\",\"X\",\"X\"],\[\"X\",\"X\",\"X\",\"X\"],\
        [\"X\",\"O\",\"X\",\"X\"]]")
