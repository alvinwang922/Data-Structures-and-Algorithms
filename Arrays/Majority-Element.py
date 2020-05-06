# Given an array of size n, find the majority element.
# The majority element is the element that appears more
# than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the
# majority element always exist in the array.


class Solution(object):
    def majorityElement(self, nums):
        if len(nums) < 3:
            return nums[0]
        counter = 0
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                counter += 1
                if counter >= len(nums)/2:
                    return nums[i]
            else:
                counter = 0


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(majorityElement([1]))
print("The values above should be 3, 2, and 1.")
