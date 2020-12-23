"""
Write an efficient algorithm that searches for a 
value in an m x n matrix. This matrix has the 
following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the 
last integer of the previous row.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]],
                     target: int):
        if not matrix:
            return False
        w, h = len(matrix[0]), len(matrix)
        left, right = 0, w * h - 1
        while left <= right:
            mid = (left + right) // 2
            curr = matrix[mid // w][mid % w]
            if curr == target:
                return True
            elif curr < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20],
                        [23, 30, 34, 50]], 3))
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20],
                        [23, 30, 34, 50]], 13))
    print(searchMatrix([], 0))
    print("The booleans above should be True, False, and False.")
