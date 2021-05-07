"""
Given an array of integers and an integer k, you need to find 
the total number of continuous subarrays whose sum equals to k.
"""


def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums-k, 0)
        d[sums] = d.get(sums, 0) + 1
    return count


print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 4))
print(subarraySum([1, 2, 3], 6))
print("The values above should be 2, 0, and 1.")
