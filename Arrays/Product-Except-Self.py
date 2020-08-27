"""
Given an array nums of n integers where n > 1, return an array 
output such that output[i] is equal to the product of all the 
elements of nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums: List[int]):
        tracker = 1
        final = []
        for i in range(len(nums)):
            final.append(tracker)
            tracker *= nums[i]
        tracker = 1
        for i in range(len(nums) - 1, -1, -1):
            final[i] *= tracker
            tracker *= nums[i]
        return final


print(productExceptSelf([1, 2, 3]))
print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([3, 4, 5, 6]))
print("The arrays above should be [6, 3, 2], [24, 12, 8, 6], \
    and [120, 90, 72, 60].")
