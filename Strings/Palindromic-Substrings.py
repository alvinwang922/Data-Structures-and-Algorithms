"""
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different 
substrings even they consist of same characters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        number = 0
        for i in range(len(s)):
            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            number += ((end - start) // 2)
            start, end = i, i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            number += ((end - start) // 2)
        return number


print(countSubstrings("abc"))
print(countSubstrings("aaa"))
print(countSubstrings("abcbe"))
print("The integers above should be 3, 6, and 6.")
