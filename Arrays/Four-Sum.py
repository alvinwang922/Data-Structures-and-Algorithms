"""
Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that 
a + b + c + d = target? Find all unique quadruplets in 
the array which gives the sum of target. Notice that the 
solution set must not contain duplicate quadruplets.
"""


def fourSum(nums: List[int], target: int):
    def nSum(nums, target, N, result, ans):
        if len(nums) < N or N < 2 or target < nums[0] \
                * N or target > nums[-1] * N:
            return
        if N == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                currSum = nums[left] + nums[right]
                if currSum == target:
                    ans.append(result +
                               [nums[left], nums[right]])
                    left += 1
                    while left < right and \
                            nums[left] == nums[left - 1]:
                        left += 1
                elif currSum < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(len(nums) - N + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    nSum(nums[i + 1:], target - nums[i],
                         N - 1, result + [nums[i]], ans)

    ans = []
    nSum(sorted(nums), target, 4, [], ans)
    return ans


print(fourSum([], 0))
print(fourSum([1, 0, -1, 2, 2, 2], 4))
print(fourSum([1, 0, -1, 0, -2, 2], 0))
print("The arrays above should be [], [[-1, 1, 2, 2]], \
    and [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]].")
