"""
Given an array arr, replace every element in that 
array with the greatest element among the elements 
to its right, and replace the last element with -1.
After doing so, return the array.
"""


def replaceElements(arr: List[int]):
    currMax = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], currMax = currMax, \
            max(currMax, arr[i])
    return arr


print(replaceElements([1]))
print(replaceElements([17, 18, 5, 4, 6, 1]))
print(replaceElements([5, 4, 3, 2, 1]))
print("The arrays above should be [-1], \
    [18, 6, 6, 6, 1, -1], and [4, 3, 2, 1, -1].")
