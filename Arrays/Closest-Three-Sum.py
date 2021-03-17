"""
Given an array nums of n integers and an integer target, find 
three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each 
input would have exactly one solution.
"""


def threeSumClosest(nums: List[int], target: int):
    nums.sort()
    ans = nums[0] + nums[1] + nums[2]
    l = len(nums)
    for i in range(l - 2):
        left, right = i + 1, l - 1
        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            if currSum == target:
                return currSum
            if abs(currSum - target) < abs(ans - target):
                ans = currSum
            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
    return ans


print(threeSumClosest([-1, 2, 1, -4], 1))
print(threeSumClosest([4, 2, 3, 2], 8))
print(threeSumClosest([5, 6, 7], 2))
print("The values above should be 2, 8, and 18.")
