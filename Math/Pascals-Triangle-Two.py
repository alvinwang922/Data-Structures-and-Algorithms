"""
Given an integer rowIndex, return the rowIndexth 
row of the Pascal's triangle.
Notice that the row index starts from 0.
"""


class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        ans = [1, 1]
        for _ in range(rowIndex - 1):
            currRow = [1]
            for i in range(len(ans) - 1):
                currRow.append(ans[i] + ans[i + 1])
            ans = currRow + [1]
        return ans

    # More time efficient solution
    def getRow2(self, rowIndex: int):
        ans = [1]
        for _ in range(rowIndex):
            ans = [x + y for x, y in
                   zip([0] + ans, ans + [0])]
        return ans

    print(getRow(0))
    print(getRow(1))
    print(getRow(5))
    print("The arrays above should be [1], [1, 1], \
        and [1, 5, 10, 10, 5, 1].")
