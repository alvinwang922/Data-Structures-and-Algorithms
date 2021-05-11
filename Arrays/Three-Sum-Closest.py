"""
Given an array nums of n integers and an integer target, find three integers 
in nums such that the sum is closest to target. Return the sum of the three 
integers. You may assume that each input would have exactly one solution.
"""


def threeSumClosest(nums: List[int], target: int):
    if len(nums) <= 3:
        return sum(nums)
    nums.sort()
    tempAns = nums[0] + nums[1] + nums[2]
    ans = tempAns
    print(nums)
    for i in range(len(nums) - 2):
        if i == 0 or nums[i] != nums[i - 1]:
            left, right = i + 1, len(nums) - 1
            while left < right:
                tempAns = nums[i] + nums[left] + nums[right]
                if tempAns < target:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif tempAns > target:
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                else:
                    return tempAns
                if abs(target - tempAns) < abs(target - ans):
                    ans = tempAns
    return ans


print(threeSumClosest([-1, 2, 1, -4], 1))
print(threeSumClosest([1, 2, 5, 10, 11], 12))
print(threeSumClosest([5, 2, 5, 10, 10, 11], 15))
print("The values above should be 2, 13, and 17.")
