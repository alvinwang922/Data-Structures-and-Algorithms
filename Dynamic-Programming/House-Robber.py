# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security system connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount
# of money of each house, determine the maximum amount of money
# you can rob tonight without alerting the police.


class maxLoot(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            nums[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                nums[i] = nums[i] + nums[i-2]
                nums[i] = max(nums[i], nums[i-1])
        return nums[len(nums)-1]


print(maxLoot([1, 2, 3, 4, 5]))
print(maxLoot([7, 1, 1, 8, 1, 9]))
print(maxLoot([10, 4, 3, 4, 1, 6]))
print("The values above should be 9, 24, and 20.")
