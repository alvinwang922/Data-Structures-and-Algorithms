# Given an unsorted integer array, find the smallest missing positive integer.


class Solution:
    def firstMissingPositive(self, nums: List[int]):
        nums = Counter(nums)
        missing = 1
        while nums[missing] >= 1:
            missing += 1
        return missing


print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([7, 8, 9, 11, 12]))
print("The values above should be 3, 2, and 1.")
