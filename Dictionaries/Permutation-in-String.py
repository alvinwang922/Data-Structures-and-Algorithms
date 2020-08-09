"""
Given two strings s1 and s2, write a function to return true if s2 
contains the permutation of s1. In other words, one of the first 
string's permutations is the substring of the second string.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str):
        s1Letters = Counter(s1)
        s2Letters = Counter(s2[:len(s1)])
        tracker = 0
        for i in range(len(s1), len(s2) + 1):
            if s1Letters == s2Letters:
                return True
            s2Letters[s2[tracker]] -= 1
            if s2Letters[s2[tracker]] <= 0:
                s2Letters.pop(s2[tracker])
            if i < len(s2):
                s2Letters[s2[i]] += 1
            tracker += 1
        return False


print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))
print(checkInclusion("abcd", "abicdbaooo"))
print("The booleans above should be True, False, and True.")
