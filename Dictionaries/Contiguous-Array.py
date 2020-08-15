"""
Given a binary array, find the maximum length of a contiguous 
subarray with equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]):
        counter = {0: 0}
        tracker = 0
        maxLength = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tracker -= 1
            else:
                tracker += 1
            if tracker not in counter:
                counter[tracker] = i + 1
            else:
                maxLength = max(maxLength, i + 1 - counter[tracker])
        return maxLength


print(findMaxLength([0, 1]))
print(findMaxLength([0, 1, 0]))
print(findMaxLength([0, 1, 0, 1, 0, 0, 0, 1]))
print("The values above should be 2, 2, and 4.")
