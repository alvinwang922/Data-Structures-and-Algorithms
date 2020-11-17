"""
Given an integer array nums, design an algorithm to randomly shuffle the array.
Implement the Solution class:
Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
"""

import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        shuffled = []
        copy = self.nums[:]
        for i in range(len(self.nums) - 1, -1, -1):
            index = random.randint(0, i)
            shuffled.append(copy[index])
            copy.pop(index)
        return shuffled

    # better shuffle
    def shuffle2(self):
        """
        Returns a random shuffling of the array.
        """
        return sorted(self.nums, key=lambda x: random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

"""
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
"""
