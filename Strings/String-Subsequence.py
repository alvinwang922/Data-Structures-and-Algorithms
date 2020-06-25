"""
Given a string s and a string t, check if s is subsequence of t. A subsequence 
of a string is a new string which is formed from the original string by 
deleting some (can be none) of the characters without disturbing the 
relative positions of the remaining characters. (ie, "ace" is a subsequence 
of "abcde" while "aec" is not).
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        tracker = 0
        for char in t:
            if char == s[tracker]:
                tracker += 1
            if tracker == len(s):
                return True
        return False


print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("", "abc"))
print("The booleans above should be True, False, and True.")
