"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in range(len(s)):
            tempChar = s[i]
            left = i
            right = i
            while left >= 0 and s[left] == tempChar:
                left -= 1
            while right < len(s) and s[right] == tempChar:
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            if right - left > end - start:
                start = left
                end = right
        return s[start:end]


print(longestPalindrome("babad"))
print(longestPalindrome("cbba"))
print(longestPalindrome("abcdeeeeeedcja"))
print("The strings above should be \"bab\", \"bb\", and \"cdeeeeeedc\".")
