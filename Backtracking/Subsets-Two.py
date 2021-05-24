"""
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""


def subsetsWithDup(nums: List[int]):
    res = []
    nums.sort()
    backtrack(nums, [], res)
    return res


def backtrack(nums, subset, res):
    res.append(subset)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        backtrack(nums[i+1:], subset + [nums[i]], res)


print(subsetsWithDup([1, 2, 2]))
print(subsetsWithDup([1, 2, 4, 4]))
print(subsetsWithDup([]))
print("The arrays above should be [[], [1], [1, 2], [1, 2, 2], [2]], [2, 2]], \
    [[], [1], [1, 2], [1, 2, 4], [1, 2, 4, 4], [1, 4], [1, 4, 4], [2], [2, 4], \
        [2, 4, 4], [4], [4, 4]], and [[]].")
