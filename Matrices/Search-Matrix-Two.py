"""
Write an efficient algorithm that searches for a target value in 
an m x n integer matrix. The matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False

    print(searchMatrix([[0]], 1))
    print(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19],
                        [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
                        [18, 21, 23, 26, 30]], 5))
    print(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19],
                        [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
                        [18, 21, 23, 26, 30]], 20))
    print("The booleans above should be False, True, and False.")
