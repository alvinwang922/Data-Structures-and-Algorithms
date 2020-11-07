"""
Write a function to find the longest common prefix string 
amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        ans, i = "", 0
        if not strs or not strs[0]:
            return ans
        if len(strs) == 1:
            return strs[0]
        while True:
            if i < len(strs[0]):
                curr = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != curr:
                    return ans
            i += 1
            ans += curr
        return ans


# Faster solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if not strs:
            return ""
        str1, str2 = min(strs), max(strs)
        for i, c in enumerate(str1):
            if c != str2[i]:
                return str1[:i]
        return str1

    print(longestCommonPrefix(["flower", "flower", "flower", "flower"]))
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog", "racecar", "car"]))
    print("The strings above should be \"flower\", \"fl\", and \"\".")
