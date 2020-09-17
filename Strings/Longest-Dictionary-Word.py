"""
Given a string and a string dictionary, find the longest string in the 
dictionary that can be formed by deleting some characters of the given 
string. If there are more than one possible results, return the longest 
word with the smallest lexicographical order. If there is no possible 
result, return the empty string.
"""


class Solution:
    def findLongestWord(self, s: str, d: List[str]):
        ans = ""
        for word in d:
            i = 0
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
            if i == len(word):
                if (len(word) > len(ans)):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word
        return ans


print(findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(findLongestWord("abpcplea", ["a", "b", "c"]))
print(findLongestWord("aaa", ["aaa", "aa", "a"]))
print("The strings above should be \"apple\", \"a\", and \"aaa\".")
