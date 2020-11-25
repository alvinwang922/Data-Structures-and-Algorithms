"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined 
by its upper left corner (row1, col1) and lower right corner (row2, col2).
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        for i in range(len(matrix)):
            currSum = 0
            for j in range(len(matrix[0])):
                currSum += matrix[i][j]
                if i == 0:
                    matrix[i][j] = currSum
                else:
                    matrix[i][j] = matrix[i - 1][j] + currSum
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        else:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1] \
                - self.matrix[row1 - 1][col2] + self.matrix[row1 - 1][col1 - 1]


"""
Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(row1,col1,row2,col2)

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""
