"""
Given two words word1 and word2, find the minimum number of 
operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character
"""


class Solution:
    def minDistance(self, word1: str, word2: str):
        twoLength = len(word2)
        tracker = list(range(twoLength + 1))
        for i in range(len(word1)):
            prev, tracker = tracker, [i+1] + [0] * twoLength
            for j in range(twoLength):
                if word1[i] == word2[j]:
                    tracker[j + 1] = prev[j]
                else:
                    tracker[j + 1] = min(tracker[j], prev[j], prev[j+1]) + 1
        return tracker[twoLength]


print(minDistance("horse", "ros"))
print(minDistance("intention", "execution"))
print(minDistance("horse", "horse"))
print("The values above should be 3, 5, and 0.")
