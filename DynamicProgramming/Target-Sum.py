"""
You are given a list of non-negative integers, a1, a2, ..., an, 
and a target, S. Now you have 2 symbols + and -. For each integer, 
you should choose one from + and - as its new symbol.
Find out how many ways to assign symbols to make sum of integers 
equal to target S.
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int):
        self.memo = {}
        return self.dp(nums, S, len(nums) - 1, 0)

    def dp(self, nums, S, index, currSum):
        if (index, currSum) in self.memo:
            return self.memo[(index, currSum)]
        if index < 0 and currSum == S:
            return 1
        if index < 0:
            return 0
        positive = self.dp(nums, S, index - 1, currSum + nums[index])
        negative = self.dp(nums, S, index - 1, currSum - nums[index])
        self.memo[(index, currSum)] = positive + negative
        return self.memo[(index, currSum)]


print(findTargetSumWays([1, 1, 1, 1, 1], 3))
print(findTargetSumWays([1, 1, 1, 1, 1], 4))
print(findTargetSumWays([1, 1, 1, 1, 2], 4))
print("The values above should be 5, 0, and 4.")
