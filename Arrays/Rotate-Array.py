"""
Given an array, rotate the array to the right by k 
steps, where k is non-negative.
Follow up:
Try to come up as many solutions as you can, there 
are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution:
    def rotate(self, nums: List[int], k: int):
        k = k % len(nums)
        nums[:-k] = nums[:-k][::-1]
        nums[-k:] = nums[-k:][::-1]
        nums[:] = nums[::-1]
        return nums


# Another solution
class Solution:
    def rotate(self, nums: List[int], k: int):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([-1, -100, 3, 99], 2))
print(rotate([1, 2, 3], 4))
print("The arrays above should be [5, 6, 7, 1, 2, 3, 4], \
    [3, 99, -1, -100], and [3, 1, 2].")
