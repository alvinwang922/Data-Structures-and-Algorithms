"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""


class Solution:
    def isAnagram(self, s: str, t: str):
        occurences = defaultdict(int)
        for char in s:
            occurences[char] += 1
        for char in t:
            occurences[char] -= 1
        for key in occurences:
            if occurences[key] != 0:
                return False
        return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("bot", "boot"))
print("The booleans above should be True, False, and False.")
