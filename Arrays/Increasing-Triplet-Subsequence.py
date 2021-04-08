"""
Given an unsorted array return whether an increasing 
subsequence of length 3 exists or not in the array.
"""


def increasingTriplet(nums: List[int]):
    if len(nums) < 3:
        return False
    start, mid = nums[0], float("inf")
    for i in range(1, len(nums)):
        if nums[i] < start:
            start = nums[i]
        elif start < nums[i] < mid:
            mid = nums[i]
        if nums[i] > mid:
            return True
    return False


# A cleaner solution
def increasingTriplet2(nums: List[int]):
    start = mid = float("inf")
    for n in nums:
        if n <= start:
            start = n
        elif n <= mid:
            mid = n
        else:
            return True
    return False


print(increasingTriplet([1, 2]))
print(increasingTriplet([1, 2, 3, 4, 5]))
print(increasingTriplet([5, 4, 3, 2, 1]))
print("The booleans above should be False, True, and False.")
