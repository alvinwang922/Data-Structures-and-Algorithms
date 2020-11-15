"""
Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the 
product of all the elements in the subarray is less than k.
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int):
        left, curr, ans = 0, 1, 0
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k and left <= right:
                curr /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

    print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(numSubarrayProductLessThanK([1, 1, 1, 1, 1, 1, 1], 3))
    print(numSubarrayProductLessThanK([10], 4))
    print("The values above should be 8, 28, and 0.")
