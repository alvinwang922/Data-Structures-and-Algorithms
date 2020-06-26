"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
Write the code that will take a string and make this conversion given a number of rows
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        rowTracker = 0
        forward = True
        for char in s:
            rows[rowTracker] += char
            if rowTracker == 0:
                forward = True
            elif rowTracker == numRows - 1:
                forward = False
            if forward == True:
                rowTracker += 1
            else:
                rowTracker -= 1
        return "".join(rows)


print(convert("PAYPALISHIRING", 1))
print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print("The strings above should be \"PAYPALISHIRING\", \"PAHNAPLSIIGYIR\", and \PINALSIGYAHRPI\".")