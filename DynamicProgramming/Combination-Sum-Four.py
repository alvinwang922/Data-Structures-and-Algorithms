"""
Given an integer array with all positive numbers and no 
duplicates, find the number of possible combinations that 
add up to a positive integer target.
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]
        return dp[-1]


print(combinationSum4([1, 2, 3], 4))
print(combinationSum4([1, 2, 3], 5))
print(combinationSum4([2, 4, 6], 5))
print("The values above should be 7, 13, and 0.")
