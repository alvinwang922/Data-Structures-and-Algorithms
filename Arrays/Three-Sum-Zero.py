"""
Given an array nums of n integers, are there elements
a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
"""


def threeSum(nums):
    answers = []
    nums.sort()
    if len(nums) < 3:
        return answers
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                answers.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return answers


print(threeSum([-1, 0, 1, 2, -1, -4]))
print("The array above should be [[-1, 0, 1], [-1, -1, 2]]")
