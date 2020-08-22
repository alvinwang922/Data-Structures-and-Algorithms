"""
Given two strings S and T, return if they are equal when both are typed 
into empty text editors. "#" means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
"""


class Solution:
    def backspaceCompare(self, S: str, T: str):
        newS, newT = "", ""
        for char in S:
            if char == "#":
                newS = newS[:len(newS) - 1]
            else:
                newS += char
        for char in T:
            if char == "#":
                newT = newT[:len(newT) - 1]
            else:
                newT += char
        return newS == newT


print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a##c", "#a#cd"))
print("The booleans above should be True, True, and False.")
