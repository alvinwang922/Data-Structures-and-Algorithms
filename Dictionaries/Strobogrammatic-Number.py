"""
A strobogrammatic number is a number that looks the 
same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is 
strobogrammatic. The number is represented as a string.
"""


class Solution:
    def isStrobogrammatic(self, num: str):
        match = {"0": "0", "1": "1", "6": "9",
                 "8": "8", "9": "6"}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in match or \
                    num[right] != match[num[left]]:
                return False
            left += 1
            right -= 1
        return True

    print(isStrobogrammatic(69))
    print(isStrobogrammatic(962))
    print(isStrobogrammatic(101))
    print("The booleans above should be True, False, and True.")
