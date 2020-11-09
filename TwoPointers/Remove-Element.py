"""
Given an array nums and a value val, remove all instances 
of that value in-place and return the new length.
Do not allocate extra space for another array, you must 
do this by modifying the input array in-place with O(1) 
extra memory. The order of elements can be changed. 
It doesn't matter what you leave beyond the new length.
Clarification:
Confused why the returned value is an integer but your 
answer is an array? Note that the input array is passed 
in by reference, which means a modification to the input 
array will be known to the caller as well.
"""


class Solution:
    def removeElement(self, nums: List[int], val: int):
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left

    print(removeElement([3, 2, 2, 3], 3))
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(removeElement([1, 2, 3, 4], 5))
    print("The values above should be 2, 5, and 4.")
