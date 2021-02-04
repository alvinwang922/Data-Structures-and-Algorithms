"""
Given two words (beginWord and endWord), and a dictionary's word list, find the 
length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""

import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

        print(ladderLength("hit", "cog", ["hot", "dot", "dog",
                                          "lot", "log", "cog"]))
        print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
        print(ladderLength("lol", "dol", ["hot", "dog", "dol"]))
        print("The values above should be 5, 0, and 2.")
