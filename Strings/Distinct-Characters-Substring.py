"""
Given a string s , find the length of the longest substring t 
that contains at most 2 distinct characters.
"""


import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str):
        length = len(s)
        if length < 3:
            return length
        ans, left, right = 0, 0, 0
        while right < length:
            right, start = left, left
            letters, tracker = set(), True
            while right < length:
                letters.add(s[right])
                if len(letters) == 3:
                    ans = max(ans, right - start)
                    break
                elif tracker and len(letters) == 2:
                    left = right
                    tracker = False
                right += 1
        ans = max(ans, right - start)
        return ans

    # faster solution using dictionaries
    def lengthOfLongestSubstringTwoDistinct2(self, s: str):
        length = len(s)
        if length < 3:
            return length
        ans, right = 1, 0
        tracker = collections.defaultdict(int)
        for left in range(length):
            while right < length and len(tracker) <= 2:
                tracker[s[right]] += 1
                right += 1
            if right >= length and len(tracker) <= 2:
                ans = max(ans, right - left)
            else:
                ans = max(ans, right - left - 1)
            tracker[s[left]] -= 1
            if tracker[s[left]] == 0:
                del tracker[s[left]]
        return ans

    print(lengthOfLongestSubstringTwoDistinct("eceba"))
    print(lengthOfLongestSubstringTwoDistinct("ccaabbb"))
    print(lengthOfLongestSubstringTwoDistinct("aaab"))
    print("The values above should be 3, 5, and 4.")
