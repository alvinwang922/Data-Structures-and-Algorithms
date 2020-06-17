"""
Given a sorted array and a target value, return the index if the target 
is found. If not, return the index where it would be if it were inserted 
in order. You may assume no duplicates in the array.
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
print(searchInsert([1, 3, 5, 6], 0))
print("The values above should be 2, 1, 4, and 0.")
