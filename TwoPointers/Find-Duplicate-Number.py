"""
Given an array of integers nums containing n + 1 integers where 
each integer is in the range [1, n] inclusive. There is only one 
duplicate number in nums, return this duplicate number.
Follow-ups:
How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
"""


class Solution:
    def findDuplicate(self, nums: List[int]):
        if len(nums) < 2:
            return -1
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


print(findDuplicate([1, 3, 4, 2, 2]))
print(findDuplicate([3, 1, 3, 4, 2]))
print(findDuplicate([1, 1, 2]))
print("The values above should be 2, 3, and 1.")
