"""
Given a sorted array of integers, return an array of integers
containing all unique integers from the original array.
Do so with O(1) space complexity.
"""


def uniqueIntegers(arr):
      uniqueIndex = 1
  for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
      arr[i], arr[uniqueIndex] = arr[uniqueIndex], arr[i]
      uniqueIndex += 1
  return arr[0:uniqueIndex]


print(uniqueIntegers([[0,1,1,1,3]))
print(uniqueIntegers([[0,1,3]))
print(uniqueIntegers([[0,0,0,0,0]))
print("The arrays above should be [0,1,3], [0,1,3], and [0].")
