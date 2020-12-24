"""
Given a column title as appear in an Excel sheet, 
return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
"""


class Solution:
    def titleToNumber(self, s: str):
        ans = 0
        for char in s:
            ans = ans * 26 + ord(char) - 64
        return ans

    print(titleToNumber("A"))
    print(titleToNumber("AB"))
    print(titleToNumber("ZY"))
    print("The values above should be 1, 28, and 701.")
