"""
Given an array of integers nums and an integer limit, return the size 
of the longest non-empty subarray such that the absolute difference 
between any two elements of this subarray is less than or equal to limit.
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int):
        left, right, currMin, currMax, ans = 0, 0, nums[0], nums[0], 1
        while right < len(nums):
            currMin = min(currMin, nums[right])
            currMax = max(currMax, nums[right])
            if abs(currMax - currMin) <= limit:
                ans = max(ans, right - left + 1)
            else:
                if nums[left] == currMin:
                    currMin = min(nums[left + 1: right + 1])
                if nums[left] == currMax:
                    currMax = max(nums[left + 1: right + 1])
                left += 1
            right += 1
        return ans

    print(longestSubarray([8, 2, 4, 7], 4))
    print(longestSubarray([10, 1, 2, 4, 7, 2], 5))
    print(longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
    print("The values above should be 2, 4, and 3.")
