"""
Given an array of strings, group anagrams together.
Note: All inputs will be in lowercase.
The order of your output does not matter.
"""

import collections


def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[tuple(sorted(word))].append(word)
    return anagrams.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print("The return value above should be \
[[\"ate\", \"eat\", \"tea\"], [\"nat\", \"tan\"], [\"bat\"]].")
