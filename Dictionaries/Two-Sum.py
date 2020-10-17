"""
Given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int):
        if len(nums) <= 1:
            return False
        tracker = dict()
        for i in range(len(nums)):
            if nums[i] in tracker:
                return [tracker[nums[i]], i]
            else:
                tracker[target - nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print("The arrays above should be [0, 1], [1, 2], and [0, 1].")
