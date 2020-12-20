"""
Given an array of integers nums sorted in ascending 
order, find the starting and ending position of a 
given target value. If target is not found in the 
array, return [-1, -1].
Follow up: Could you write an algorithm with 
O(log n) runtime complexity?
"""


class Solution:
    def searchRange(self, nums: List[int], target: int):
        def findStart(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findEnd(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        start, end = findStart(nums, target), \
            findEnd(nums, target)
        if start <= end:
            return [start, end]
        return [-1, -1]

    print(searchRange([5, 7, 7, 8, 8, 10], 6))
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
    print(searchRange([], 0))
    print("The arrays above should be [-1, -1], \
        [3, 4], and [-1, -1]")
