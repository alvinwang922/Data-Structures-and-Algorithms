"""
Given an array nums with n objects colored red, white, or 
blue, sort them in-place so that objects of the same color 
are adjacent, with the colors in the order red, white, and 
blue. Here, we will use the integers 0, 1, and 2 to 
represent the color red, white, and blue respectively.
Follow up:
Could you solve this problem without using the library's 
sort function? Could you come up with a one-pass algorithm 
using only O(1) constant space?
"""


class Solution:
    def sortColors(self, nums: List[int]):
        left, right, i = 0, len(nums) - 1, 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
        return nums


print(sortColors([2, 0, 2, 1, 1, 0]))
print(sortColors([2, 0, 1]))
print(sortColors([0]))
print("The arrays above should be [0, 0, 1, 1, 2, 2], \
    [0, 1, 2], and [0].")
