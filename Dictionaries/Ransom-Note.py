"""
Given an arbitrary ransom note string and another string containing letters from 
ll the magazines, write a function that will return true if the ransom note can 
be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        magChars = defaultdict(int)
        for char in magazine:
            magChars[char] += 1
        for char in ransomNote:
            if magChars[char] == 0:
                return False
            else:
                magChars[char] -= 1
        return True

    # A more efficient method
    def canConstruct2(self, ransomNote: str, magazine: str):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
print("The booleans above should be False, False, and True.")
