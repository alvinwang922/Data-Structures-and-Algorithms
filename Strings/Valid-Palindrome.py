"""
Given a string, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        while front < back:
            while front < back and not s[front].isalnum():
                front += 1
            while front < back and not s[back].isalnum():
                back -= 1
            if s[front].lower() != s[back].lower():
                return False
            front += 1
            back -= 1
        return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("0P"))
print("The booleans above should be True, False, and False.")
