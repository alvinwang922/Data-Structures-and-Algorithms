"""
In an alien language, surprisingly they also use english lowercase letters, 
but possibly in a different order. The order of the alphabet is some 
permutation of lowercase letters. Given a sequence of words written in 
the alien language, and the order of the alphabet, return true if and 
only if the given words are sorted lexicographicaly in this alien language.
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str):
        order = {char: i for i, char in enumerate(order)}
        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False
            for char1, char2 in zip(word1, word2):
                if order[char1] < order[char2]:
                    break
                elif order[char1] > order[char2]:
                    return False
        return True


print(isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
print("The booleans above should be True, False, and False.")
