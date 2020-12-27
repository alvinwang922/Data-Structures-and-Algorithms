"""
Given an array of integers arr, return true if and only 
if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""


class Solution:
    def validMountainArray(self, arr: List[int]):
        if len(arr) < 3:
            return False
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] < arr[left + 1]:
                left += 1
            elif arr[right] < arr[right - 1]:
                right -= 1
            else:
                break
        return (left != 0) and (right != len(arr) - 1) \
            and (left == right)

    print(validMountainArray([2, 1]))
    print(validMountainArray([3, 5, 5]))
    print(validMountainArray([0, 3, 2, 1]))
    print("The booleans above should be False, False, and True.")
