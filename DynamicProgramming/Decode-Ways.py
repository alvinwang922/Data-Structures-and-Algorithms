"""
A message containing letters from A-Z is being 
encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits,
determine the total number of ways to decode it.
"""


class Solution(object):
    def numDecodings(self, s):
        if s is "":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


print(numDecodings("12"))
print(numDecodings("226"))
print(numDecodings("12321"))
print("The values above should be 2, 3, and 6.")
