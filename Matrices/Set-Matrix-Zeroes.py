"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in-place.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = set()
        y = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x.add(i)
                    y.add(j)
        for i in x:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in y:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        print(matrix)


print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(setZeroes([[0, 1, 1]]))
print("The matrices above should be [[1, 0, 1], [0, 0, 0], [1, 0, 1]], \
    [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], and [[0, 0, 0]].")
