"""
Implement next permutation, which rearranges numbers into the 
lexicographically next greater permutation of numbers. If such 
arrangement is not possible, it must rearrange it as the lowest 
possible order (ie, sorted in ascending order). The replacement 
must be in-place and use only constant extra memory.
"""


def nextPermutation(nums: List[int]):
    # Do not return anything, modify nums in-place instead.
    i = j = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1
    if i == 0:
        nums.reverse()
    else:
        k = i - 1
        while nums[k] >= nums[j]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        front, end = k + 1, len(nums) - 1
        while front < end:
            nums[front], nums[end] = nums[end], nums[front]
            front += 1
            end -= 1


print(nextPermutation([1, 2, 3]))
print(nextPermutation([3, 2, 1]))
print(nextPermutation([1, 1, 5]))
print("The arrays above should be [1, 3, 2], [1, 2, 3], and [1, 5, 1].")
