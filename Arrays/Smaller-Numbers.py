"""
Given the array nums, for each nums[i] find out how many numbers in 
the array are smaller than it. That is, for each nums[i] you have to 
count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
"""


from collections import Counter, defaultdict


def smallerNumbersThanCurrent(nums: List[int]):
    count = Counter(nums)
    tracker = defaultdict(int)
    sort = sorted(nums)
    curr = 0
    visited = set()
    for num in sort:
        if num not in visited:
            tracker[num] = curr
            curr += count[num]
            visited.add(num)
    for i in range(len(nums)):
        nums[i] = tracker[nums[i]]
    return nums


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(smallerNumbersThanCurrent([6, 5, 4, 8]))
print(smallerNumbersThanCurrent([7, 7, 7, 7]))
print("The arrays above should be [4, 0, 1, 1, 3], [2, 1, 0, 3], \
and [0, 0, 0, 0].")
