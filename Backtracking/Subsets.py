"""
Given a set of distinct integers, nums, return all possible 
subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""


def subsets(nums: List[int]):
    res = []
    backtrack(nums, [], res)
    return res


def backtrack(nums, subset, res):
    res.append(subset)
    for i in range(len(nums)):
        backtrack(nums[i+1:], subset + [nums[i]], res)


print(subsets([]))
print(subsets([1, 2]))
print(subsets([1, 2, 3]))
print("The arrays above should be [[]], [[], [1], [2], [1, 2]], and \
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]")
