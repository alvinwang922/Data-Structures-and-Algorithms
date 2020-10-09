"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the 
digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not 
necessarily solvable. Only the filled cells need to be validated 
according to the mentioned rules.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        tracker = defaultdict(set)
        for i in range(len(board)):
            temp = set()
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in temp:
                    return False
                temp.add(board[i][j])
                if board[i][j] != "." and board[i][j] in tracker[j]:
                    return False
                tracker[j].add(board[i][j])
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                temp = set()
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != "." and \
                                board[i + k][j + l] in temp:
                            return False
                        temp.add(board[i + k][j + l])
        return True


print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
print(isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
print(isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
print("The booleans above should be True, False, and False.")
