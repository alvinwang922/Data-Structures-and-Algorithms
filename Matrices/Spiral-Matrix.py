"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]):
        if not matrix:
            return
        direction = "right"
        counter = len(matrix) * len(matrix[0])
        final = []
        i = 0
        j = 0
        while counter > 0:
            final.append(matrix[i][j])
            matrix[i][j] = "visited"
            counter -= 1
            if direction == "right" and (j == len(matrix[0]) - 1or matrix[i][j + 1] == "visited"):
                direction = "down"
            elif direction == "down" and (i == len(matrix) - 1 or matrix[i + 1][j] == "visited"):
                direction = "left"
            elif direction == "left" and (j == 0 or matrix[i][j - 1] == "visited"):
                direction = "up"
            elif direction == "up" and (i == 0 or matrix[i - 1][j] == "visited"):
                direction = "right"
            if direction == "right":
                j += 1
            elif direction == "down":
                i += 1
            elif direction == "left":
                j -= 1
            elif direction == "up":
                i -= 1
        return final


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(spiralOrder([]))
print("The arrays above should be [1, 2, 3, 6, 9, 8, 7, 4, 5], \
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], and [].")
