"""
Given a sorted array nums, remove the duplicates 
in-place such that duplicates appeared at most 
twice and return the new length. Do not allocate 
extra space for another array; you must do this 
by modifying the input array in-place with O(1) 
extra memory.
"""


def removeDuplicates(nums: List[int]):
    ans = 0
    for num in nums:
        if ans < 2 or num != nums[ans - 2]:
            nums[ans] = num
            ans += 1
    return nums[:ans]


print(removeDuplicates([0, 1]))
print(removeDuplicates([1, 1, 1, 2, 2, 3]))
print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print("The arrays above should be [0, 1], \
    [1, 1, 2, 2, 3], and [0, 0, 1, 1, 2, 3, 3].")
