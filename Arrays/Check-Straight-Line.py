# You are given an array coordinates, coordinates[i] = [x, y],
# where [x, y] represents the coordinate of a point. Check if
# these points make a straight line in the XY plane.
# Constraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.


class Solution(object):
    def checkStraightLine(self, coordinates):
        isStraightLine = True
        if (coordinates[1][0] - coordinates[0][0]) == 0:
            slope = (coordinates[1][0] - coordinates[0][0]) \
                / (coordinates[1][1] - coordinates[0][1])
            for i in range(2, len(coordinates)):
                if (coordinates[i][0] - coordinates[i-1][0]) \
                        / (coordinates[i][1] - coordinates[i-1][1]) != slope:
                    isStraightLine = False
        else:
            slope = (coordinates[1][1] - coordinates[0][1]) \
                / (coordinates[1][0] - coordinates[0][0])
            for i in range(2, len(coordinates)):
                if (coordinates[i][0] - coordinates[i-1][0]) == 0:
                    isStraightLine = False
                elif (coordinates[i][1] - coordinates[i-1][1]) \
                        / (coordinates[i][0] - coordinates[i-1][0]) != slope:
                    isStraightLine = False
        return isStraightLine

    print(checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
    print(checkStraightLine([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [7, 1]]))
    print("The booleans above should be True, False, and True.")
