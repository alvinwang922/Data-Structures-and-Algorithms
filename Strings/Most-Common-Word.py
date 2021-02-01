"""
Given a paragraph and a list of banned words, return the most 
frequent word that is not in the list of banned words. It is 
guaranteed there is at least one word that isn't banned, and 
that the answer is unique. Words in the list of banned words 
are given in lowercase, and free of punctuation. Words in the 
paragraph are not case sensitive.  The answer is in lowercase.
"""

import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]):
        banned = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(word for word in words \
            if word not in banned).most_common(1)[0][0]

    print(mostCommonWord("Bob hit a ball, the hit BALL flew far \
        after it was hit.", ["hit"]))
    print("The string above should be \"ball\".")
