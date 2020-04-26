# Suppose an array sorted in ascending order is rotated
# at some pivot unknown to you beforehand.
# You are given a target value to search.
# If found in the array return its index, otherwise return -1.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# Input:  nums = [4,5,6,7,0,1,2], target = 0, output = 4
# Input: nums = [4,5,6,7,0,1,2] target = 3, output: -1


def rotatedArraySearch(nums, target):
    left = 0
    right = len(nums)-1
    # find the point where array pivots
    while left != right:
        pivot = (right - left)//2
        if nums[right] < nums[pivot]:
            left = pivot + 1
        else:
            right = pivot - 1
    if target < nums[0]:
        return binsearch(arr[left:], target) + left
    else:
        return binsearch(arr[:left], target)


print(rotatedArraySearch([[4, 5, 6, 7, 0, 1, 2]], 0))
print(rotatedArraySearch([[4, 5, 6, 7, 0, 1, 2]], 3))
print("The array above should be 4 and -1")
