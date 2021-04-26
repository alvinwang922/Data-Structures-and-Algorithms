"""
Given a sorted array nums, remove the duplicates in-place such 
that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.
"""


def removeDuplicates(nums: List[int]):
    l = len(nums)
    counter = 0
    for i in range(l - 1):
        if nums[counter] == nums[counter + 1]:
            nums.remove(nums[counter])
        else:
            counter += 1
    return len(nums)


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates([0]))
print("The values above should be 2, 5, and 1.")
