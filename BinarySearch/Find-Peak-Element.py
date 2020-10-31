"""
A peak element is an element that is greater than 
its neighbors. Given an input array nums, where 
nums[i] ≠ nums[i+1], find a peak element and return 
its index. The array may contain multiple peaks, in 
that case return the index to any one of the peaks is 
fine.You may imagine that nums[-1] = nums[n] = -∞.
"""


class Solution:
    def findPeakElement(self, nums: List[int]):
        if len(nums) < 3:
            return nums.index(max(nums))
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] \
                    and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums.index(max(nums))


print(findPeakElement([1, 2]))
print(findPeakElement([1, 2, 3, 1]))
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print("The values above should be 1, 2, and 1 or 5.")
