"""
Given an array of integers where 1 ≤ a[i] ≤ n 
(n = size of array), some elements appear twice and 
others appear once. Find all the elements of [1, n] 
inclusive that do not appear in this array. Could 
you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as 
extra space.
"""


def findDisappearedNumbers(nums: List[int]):
    for num in nums:
        idx = abs(num) - 1
        nums[idx] = -abs(nums[idx])
    return [i + 1 for i in range(len(nums))
            if nums[i] > 0]


print(findDisappearedNumbers([1, 2, 1]))
print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(findDisappearedNumbers([2, 2, 3, 3, 5, 5]))
print("The arrays above should be [3], [5, 6], and \
    [1, 4, 6].")
