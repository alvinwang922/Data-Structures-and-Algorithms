"""
You are given an integer array nums sorted in 
ascending order, and an integer target. Suppose 
that nums is rotated at some pivot unknown to 
you beforehand (i.e., [0,1,2,4,5,6,7] might 
become [4,5,6,7,0,1,2]). If target is found in 
the array return its index, otherwise, return -1.
"""


def search(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1
    while left < right:
        pivot = (left + right) // 2
        if nums[pivot] > nums[right]:
            if target > nums[pivot] or \
                    target <= nums[right]:
                left = pivot + 1
            else:
                right = pivot
        else:
            if target > nums[pivot] and \
                    target <= nums[right]:
                left = pivot + 1
            else:
                right = pivot
    if left == right and target != nums[left]:
        return -1
    return left


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1], 0))
print("The array above should be 4, -1, and -1")
