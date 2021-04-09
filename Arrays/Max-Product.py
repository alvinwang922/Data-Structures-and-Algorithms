"""
Given an integer array nums, find the contiguous subarray
within an array (containing at least one number) which
has the largest product.
"""


def maxProduct(nums):
    currentMax = nums[0]
    currentMin = nums[0]
    maxValue = currentMax
    for i in range(1, len(nums)):
        if nums[i] >= 0:
            currentMax = max(nums[i], nums[i] * currentMax)
            currentMin = min(nums[i], nums[i] * currentMin)
        if nums[i] < 0:
            temp = max(nums[i], nums[i] * currentMin)
            currentMin = min(nums[i], nums[i] * currentMax)
            currentMax = temp
        maxValue = max(currentMax, maxValue)
    return maxValue


print(maxProduct([-2, 3, -4, 5, -6]))
print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
print("The values above should be 360, 6, and 0.")
