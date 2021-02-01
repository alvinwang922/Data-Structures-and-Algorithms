"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to modify the input 
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for array in matrix:
            array.reverse()


# one line solution using zip()
class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])

    print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(rotate([[5, 1, 9, 11], [2, 4, 8, 10],
                  [13, 3, 6, 7], [15, 14, 12, 16]]))
    print(rotate([[1]]))
    print("The matrices above should be [[7, 4, 1], [8, 5, 2], [9, 6, 3]], \
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]], and [[1]].")
