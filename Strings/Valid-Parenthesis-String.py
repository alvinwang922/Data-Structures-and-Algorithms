"""
Given a string containing only three types of characters: '(', ')' and '*', 
write a function to check whether this string is valid. We define the 
validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left 
parenthesis '(' or an empty string.
An empty string is also valid.
"""


class Solution:
    def checkValidString(self, s: str):
        left = 0
        for char in s:
            if char == ")":
                if left == 0:
                    return False
                left -= 1
            else:
                left += 1
        right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                if right == 0:
                    return False
                right -= 1
            else:
                right += 1
        return True


print(checkValidString("(*)"))
print(checkValidString("())"))
print(checkValidString("(*))"))
print("The booleans above should be True, False, and True.")
