# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordEnd = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and \
                        (i-len(word) == -1 or wordEnd[i-len(word)]):
                    wordEnd[i] = True
        return wordEnd[-1]


print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("applepenapple", ["apple", "pen"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print("The booleans above should be True, True, and False.")
