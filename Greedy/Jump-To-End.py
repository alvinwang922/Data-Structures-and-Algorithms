# Given an array of non-negative integers,
# you are initially positioned at the
# first index of the array.
# Each element in the array represents your
# maximum jump length at that position.
# Determine if you are able to reach the last index.


class Solution(object):
    def canJump(self, nums):
        if len(nums) < 2:
            return True
        pointer = len(nums) - 2
        while pointer >= 0:
            if nums[pointer] == 0:
                neededJump = 1
                while neededJump > nums[pointer]:
                    neededJump += 1
                    pointer -= 1
                    if pointer < 0:
                        return False
            pointer -= 1
        return True


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([0]))
print("The values above should be true, false, and true.")
