"""
Given a string s that consists of only uppercase English letters, 
you can perform at most k operations on that string.
In one operation, you can choose any character of the string and 
change it to any other uppercase English character.
Find the length of the longest sub-string containing all repeating 
letters you can get after performing the above operations.
Note:
Both the string's length and k will not exceed 10^4.
"""


class Solution:
    def characterReplacement(self, s: str, k: int):
        count = {}
        maxLength = maxCount = start = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            maxCount = max(maxCount, count[s[end]])
            if end - start + 1 - maxCount > k:
                count[s[start]] -= 1
                start += 1
            maxLength = max(maxLength, end - start + 1)
        return maxLength


print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
print(characterReplacement("BAAAB", 2))
print("The integers above should be 4, 4, and 5.")
