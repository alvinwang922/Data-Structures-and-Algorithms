"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""


class Solution:
    def countSquares(self, matrix: List[List[int]]):
        if not matrix:
            return 0
        squares = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        squares += 1
                    else:
                        matrix[i][j] += min(matrix[i - 1][j],
                                            matrix[i][j - 1], matrix[i - 1][j - 1])
                        squares += matrix[i][j]
        return squares


print(countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))
print(countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
print(countSquares([[1]]))
print("The values above should be 15, 7, and 1.")
