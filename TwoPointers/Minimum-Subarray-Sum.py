"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the 
sum ≥ s. If there isn't one, return 0 instead.
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]):
        i, currSum, start, currAns = 0, 0, 0, float("inf")
        while i < len(nums):
            currSum += nums[i]
            i += 1
            while currSum >= s:
                currAns = min(currAns, i - start)
                currSum -= nums[start]
                start += 1
        if currAns == float("inf"):
            return 0
        return currAns


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(minSubArrayLen(100, []))
print("The values above should be 2, 3, and 0.")
