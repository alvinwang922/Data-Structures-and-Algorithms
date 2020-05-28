"""
Given a non-empty array of integers, every 
element appears three times except for one, 
which appears exactly once. Find that single one.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurrence = dict()
        for i in range(len(nums)):
            occurrence[nums[i]] = occurrence.get(nums[i], 0) + 1
        for key in occurrence:
            if occurrence[key] == 1:
                return key


print(singleNumber([2, 2, 3, 2]))
print(singleNumber([0, 1, 0, 1, 0, 1, 99]))
print(singleNumber(1))
print("The numbers above should be 3, 99, and 1.")
