# You are a professional robber planning to rob houses
# along a street. Each house has a certain amount of
# money stashed. All houses at this place are arranged
# in a circle. That means the first house is the neighbor
# of the last one. Meanwhile, adjacent houses have security
# system connected and it will automatically contact the
# police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount
# of money of each house, determine the maximum amount of money
# you can rob tonight without alerting the police.


class Solution(object):
    def robHelper(self, nums):
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = nums[i] + nums[i-2]
            nums[i] = max(nums[i], nums[i-1])
        return nums[-1]

    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) < 4:
            return max(nums)
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))


print(rob([2, 3, 2]))
print(rob([1, 2, 3, 1]))
print(rob([]))
print("The values above should be 3, 4, and 0.")
