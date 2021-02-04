"""
An image is represented by a 2-D array of integers, each integer representing 
the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of 
the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels 
connected 4-directionally to the starting pixel of the same color as the 
starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same color as the starting pixel), and so on. Replace the 
color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int):
        rows, cols, original = len(image), len(image[0]), image[sr][sc]

        def traverse(row, col):
            if (0 <= row < rows and 0 <= col < cols) \
                    and image[row][col] == original:
                image[row][col] = newColor
            else:
                return
            for (x, y) in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                traverse(row + x, col + y)
        if original != newColor:
            traverse(sr, sc)
        return image

    print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
    print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 2, 3))
    print("The matrices above should be [[2, 2, 2], [2, 2, 0], [2, 0, 1]] \
        and [[1, 1, 1], [1, 1, 3], [1, 0, 1]].")
