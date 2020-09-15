"""
Alex and Lee play a game with piles of stones. There are an even 
number of piles arranged in a row, and each pile has a positive 
integer number of stones piles[i]. The objective of the game is 
to end with the most stones.  The total number of stones is odd, 
so there are no ties. Alex and Lee take turns, with Alex starting 
first. Each turn, a player takes the entire pile of stones from 
either the beginning or the end of the row. This continues until 
there are no more piles left, at which point the person with the 
most stones wins. Assuming Alex and Lee play optimally, return 
True if and only if Alex wins the game.
"""


class Solution:
    def stoneGame(self, piles: List[int]):
        n = len(piles)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[n - 1] > 0


print(stoneGame([1, 2, 5, 5]))
print(stoneGame([5, 3, 4, 5]))
print(stoneGame([3, 2, 4, 6]))
print("The booleans above should be True, True, and True.")
