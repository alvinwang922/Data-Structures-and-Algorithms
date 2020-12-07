"""
Given a non-negative integer numRows, generate the first 
numRows of Pascal's triangle.
"""


class Solution:
    def generate(self, numRows: int):
        ans = [[1], [1, 1]]
        if numRows < 3:
            return ans[:numRows]
        for _ in range(2, numRows):
            currRow = [1]
            for i in range(len(ans[-1]) - 1):
                currRow.append(ans[-1][i] + ans[-1][i + 1])
            currRow.append(1)
            ans.append(currRow)
        return ans

    print(generate(1))
    print(generate(3))
    print(generate(5))
    print("The lists above should be [[1]], [[1], [1, 1], [1, 2, 1]], \
    and [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]].")
