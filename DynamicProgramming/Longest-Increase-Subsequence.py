# Given an unsorted array of integers, find the
# length of longest increasing subsequence.


class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        lengths = [1] * len(nums)
        for i in range(1, len(nums)):
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                j += 1
        return max(lengths)


print(lengthOfLIS([]))
print(lengthOfLIS([1, 1, 1, 1]))
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print("The values above should be 0, 1, and 4.")
