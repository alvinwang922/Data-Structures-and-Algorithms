"""
Given a non-empty string s and a dictionary wordDict containing a list 
of non-empty words, add spaces in s to construct a sentence where each 
word is a valid dictionary word. Return all such possible sentences.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]):
        return self.search(s, wordDict, {})

    def search(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.search(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res


print(wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print("The lists above should be [\"cats and dog\", \"cat sand dog\"], \
    [\"pine apple pen apple\",\"pineapple pen apple\",\"pine applepen apple\"], and [].")
