"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward 
as forward. For example, 121 is palindrome while 123 is not.
"""


from math import ceil


class Solution:
    def isPalindrome(self, x: int):
        x = str(x)
        l = len(x)
        for i in range(ceil(l // 2)):
            if x[i] != x[l - i - 1]:
                return False
        return True

    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))
    print("The booleans above should be True, \
        False, and False.")
