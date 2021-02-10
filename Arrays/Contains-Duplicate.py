"""
Given an array of integers, find if the array contains any 
duplicates. Your function should return true if any value 
appears at least twice in the array, and it should return 
false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: List[int]):
        return len(nums) != len(set(nums))

    print(containsDuplicate([1, 2, 3, 1]))
    print(containsDuplicate([1, 2, 3, 4]))
    print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print("The booleans above should be True, False, and True.")
