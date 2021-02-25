"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
"""


class Solution:
    def findDuplicates(self, nums: List[int]):
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(index + 1)
            nums[index] = -nums[index]
        return res

    print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
    print(findDuplicates([1, 3, 2, 8, 8, 2, 3, 1]))
    print(findDuplicates([1, 2, 3, 4]))
    print("The lists above should be [2,3], [8,2,3,1], and [].")
