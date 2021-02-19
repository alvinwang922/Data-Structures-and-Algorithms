"""
Given an array nums, write a function to move all 0's
to the end of it while maintaining the relative order
of the non-zero elements.
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        counter = 0
        while i < len(nums) - counter:
            if nums[i] == 0:
                counter += 1
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                i -= 1
            i += 1
        while counter > 0:
            nums[len(nums) - counter] = 0
            counter -= 1

    # Another solution

    def moveZeroes2(self, nums):
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1

    print(moveZeroes([0, 1, 0, 3, 12]))
    print(moveZeroes([0, 1, 0]))
    print(moveZeroes([0, 0, 1, 1]))
    print("The values above should be [1, 3, 12, 0, 0], [1, 0, 0], \
        and [1, 1, 0, 0].")
