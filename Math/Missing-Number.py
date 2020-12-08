"""
Given an array nums containing n distinct numbers in the 
range [0, n], return the only number in the range that 
is missing from the array.
Follow up: Could you implement a solution using only O(1) 
extra space complexity and O(n) runtime complexity?
"""


class Solution:
    def missingNumber(self, nums: List[int]):
        l = len(nums)
        return (l * (l + 1) // 2) - sum(nums)

    print(missingNumber([3, 0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([0]))
    print("The values above should be 2, 8, and 1.")
