"""
A matrix diagonal is a diagonal line of cells starting 
from some cell in either the topmost row or leftmost 
column and going in the bottom-right direction until 
reaching the matrix's end. For example, the matrix 
diagonal starting from mat[2][0], where mat is a 6 x 3 
matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
Given an m x n matrix mat of integers, sort each matrix 
diagonal in ascending order and return the resulting matrix.
"""


class Solution:
    def diagonalSort(self, mat: List[List[int]]):
        row, col = len(mat), len(mat[0])
        for i in range(row):
            self.sortRow(mat, i, 0, row, col)
        for j in range(1, col):
            self.sortRow(mat, 0, j, row, col)
        return mat

    def sortRow(self, mat, i, j, row, col):
        x, y, curr = i, j, []
        while x < row and y < col:
            curr.append(mat[x][y])
            x += 1
            y += 1
        curr.sort()
        for a in range(len(curr)):
            mat[i][j] = curr[a]
            i += 1
            j += 1

    print(diagonalSort([[1], [2], [3]]))
    print(diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
    print("The matrices above should be [[1], [2], [3]] and \
          [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]].")
