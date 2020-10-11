"""
We have a collection of rocks, each rock has a positive integer weight.
Each turn, we choose any two rocks and smash them together. Suppose the 
stones have weights x and y with x <= y.  The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of 
weight y has new weight y-x. At the end, there is at most 1 stone left. 
Return the smallest possible weight of this stone (the weight is 0 if 
there are no stones left.)
"""


class Solution:
    def lastStoneWeightII(self, stones: List[int]):
        total = sum(stones)
        dp = (total // 2 + 1) * [0]
        for stone in stones:
            for i in range(total // 2, -1, -1):
                if i >= stone:
                    dp[i] = max(stone + dp[i - stone], dp[i])
        return total - 2 * dp[-1]


print(lastStoneWeightII([2, 7, 4, 1, 8, 1]))
print(lastStoneWeightII([2, 8, 4, 4, 8, 2]))
print(lastStoneWeightII([2, 8, 4, 4, 8, 4]))
print("The values abouve should be 1, 0, and 2.")
