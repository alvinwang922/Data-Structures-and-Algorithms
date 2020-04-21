# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.


class Solution(object):
    def maxSubArray(self, nums):
        tempMax = nums[0]
        actualMax = nums[0]
        for i in range(1, len(nums)):
            tempMax = max(nums[i], tempMax+nums[i])
            actualMax = max(tempMax, actualMax)
        return actualMax


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([1, -2, 4, 5, -12, 13]))
print(maxSubArray([1, -2, 3, -4, -5]))
print("The values above should be 6, 10, and 2.")
