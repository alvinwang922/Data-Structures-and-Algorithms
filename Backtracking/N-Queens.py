"""
The n-queens puzzle is the problem of placing n queens on an n×n
chessboard such that no two queens attack each other. Given an
integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the
n-queens' placement, where 'Q' and '.' both indicate a queen and
an empty space respectively.
"""


class Solution:
    def solveNQueens(self, n: int):
        solutions = []
        self.backtrack(n, solutions, [])
        output = []
        for solution in solutions:
            board = []
            for value in solution:
                board_row = ""
                for i in range(n):
                    if value == i:
                        board_row += 'Q'
                    else:
                        board_row += '.'
                board.append(board_row)
            output.append(board)
        return output

    def backtrack(self, n, solutions, currentSolution):
        if self.conflict(currentSolution) == True:
            return
        else:
            if len(currentSolution) == n:
                solutions.append(currentSolution[:])
        for i in range(n):
            currentSolution.append(i)
            self.backtrack(n, solutions, currentSolution)
            currentSolution.pop()

    def conflict(self, solution):
        if len(solution) == 1 or len(solution) == 0:
            return False
        else:
            row = len(solution) - 1
            col = solution[row]

            for i in range(len(solution) - 1):
                if i == row or solution[i] == col or solution[i] + i \
                    == col + row or solution[i] - i == col - row:
                    return True
            return False


print(solveNQueens(4))
print(solveNQueens(3))
print("The lists above should be [[\".Q..\", \"...Q\", \"Q...\", \"..Q.\"],\
    [\"..Q.\", \"Q...\", \"...Q\", \".Q..\"]]\" and [].)
