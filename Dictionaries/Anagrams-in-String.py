"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p 
will not be larger than 20,100. The order of output does not matter.
"""


class Solution:
    def findAnagrams(self, s: str, p: str):
        final = []
        sLetters = Counter(s[:len(p)])
        pLetters = Counter(p)
        tracker = 0
        for i in range(len(p), len(s) + 1):
            if sLetters == pLetters:
                final.append(tracker)
            sLetters[s[tracker]] -= 1
            if sLetters[s[tracker]] <= 0:
                sLetters.pop(s[tracker])
            if i < len(s):
                sLetters[s[i]] += 1
            tracker += 1
        return final


print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("abab", "ab"))
print(findAnagrams("abccbaabcab", "abc"))
print("The arrays above should be [0, 6], [0, 1, 2], and [0, 3, 6, 7, 8].")
