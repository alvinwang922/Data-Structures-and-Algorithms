"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ["(", "{", "["]
        closes = [")", "}", "]"]
        for char in s:
            if char in opens:
                stack.append(char)
            elif char in closes:
                if not stack or opens[closes.index(char)] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
print("The booleans above should be True, True, False, False, and True.")
