"""
Given an m x n matrix, return true if the matrix is Toeplitz. 
Otherwise, return false. A matrix is Toeplitz if every diagonal 
from top-left to bottom-right has the same elements.
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]):
        if not matrix or len(matrix) == 1:
            return True
        length = len(matrix[0])
        for i in range(1, len(matrix)):
            if matrix[i][1:length] != matrix[i-1][0:length-1]:
                return False
        return True

    print(isToeplitzMatrix([[1]]))
    print(isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
    print(isToeplitzMatrix([[1, 2], [2, 2]]))
    print("The booleans above should be True, True, and False.")
