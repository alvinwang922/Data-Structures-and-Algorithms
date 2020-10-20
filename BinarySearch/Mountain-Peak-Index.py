"""
Let's call an array arr a mountain if the following properties 
hold: arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, 
return any i such that arr[0] < arr[1] < ... arr[i - 1] < 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]):
        left, right = 0, len(arr) - 1
        while right > left:
            target = (left + right) // 2
            if arr[target] > arr[target - 1] and \
                    arr[target] > arr[target + 1]:
                return target
            elif arr[target] <= arr[target - 1]:
                right = target
            elif arr[target] >= arr[target - 1]:
                left = target


# another solution
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]):
        return arr.index(max(arr))


print(peakIndexInMountainArray([0, 10, 5, 2]))
print(peakIndexInMountainArray([3, 4, 5, 1]))
print(peakIndexInMountainArray([24, 69, 100, 99, 79,
                                78, 67, 36, 26, 19]))
print("The values above should be 1, 2, and 2.")
