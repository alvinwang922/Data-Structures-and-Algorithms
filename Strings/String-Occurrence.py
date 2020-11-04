"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str):
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))
print(strStr("", ""))
print("The values above should be 2, -1, and 0.")
