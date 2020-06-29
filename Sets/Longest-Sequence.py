"""
Given an unsorted array of integers, find the length of the longest consecutive 
elements sequence. Uour algorithm should run in O(n) complexity.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLength = 0
        for num in nums:
            if num - 1 not in nums:
                end = num + 1
                while end in nums:
                    end += 1
                maxLength = max(maxLength, end - num)
        return maxLength


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([]))
print(longestConsecutive([2, 4, 1, 5]))
print("The numbers above should be 4, 0, and 2.")
