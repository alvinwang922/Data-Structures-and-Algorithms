"""
Given a fixed length array arr of integers, 
duplicate each occurrence of zero, shifting 
the remaining elements to the right.
Note that elements beyond the length of the 
original array are not written.
"""


def duplicateZeros(arr: List[int]):
    zeros = 0
    for num in arr:
        if num == 0:
            zeros += 1
    length = len(arr)
    for i in range(length - 1, -1, -1):
        if i + zeros < length:
            arr[i + zeros] = arr[i]
        if arr[i] == 0:
            zeros -= 1
            if i + zeros < length:
                arr[i + zeros] = 0
    return arr


print(duplicateZeros([0]))
print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicateZeros([1, 2, 3]))
print("The lists above should be [0], \
    [1, 0, 0, 2, 3, 0, 0, 4], and [1, 2, 3].")
