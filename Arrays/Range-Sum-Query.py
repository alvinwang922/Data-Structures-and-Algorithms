"""
Given an integer array nums, find the sum of the elements 
between indices i and j (i ≤ j), inclusive.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer 
array nums. int sumRange(int i, int j) Return the sum of the 
elements of the nums array in the range [i, j] inclusive 
(i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
"""


class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.currSum = [nums[0]]
        for num in nums[1:]:
            self.currSum.append(self.currSum[-1] + num)

    def sumRange(self, i: int, j: int):
        return self.currSum[j] if i == 0 else self.currSum[j] \
            - self.currSum[i - 1]


"""
Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
param_1 = obj.sumRange(i,j)
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
[null, 1, -1, -3]
"""
