"""
Given a string, find the length of the longest substring without 
repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        length = 1
        start = 0
        end = 1
        while end < len(s):
            while end < len(s) and s[end] not in s[start:end]:
                end += 1
            length = max(length, end - start)
            if end < len(s):
                start = s.index(s[end], start, end) + 1
                end += 1
        return length

    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print("The integers above should be 3, 1, and 3.")
