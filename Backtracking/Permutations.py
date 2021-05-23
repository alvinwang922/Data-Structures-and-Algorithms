# Given a collection of distinct integers, return all possible permutations.


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    backtrack(nums, [], res)
    return res


def backtrack(nums, permutations, res):
    if not nums:
        res.append(permutations)
    else:
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:],
                      permutations + [nums[i]], res)


print(permute([]))
print(permute([1, 2]))
print(permute([1, 2, 3]))
print("The arrays above should be [], [[1, 2], [2, 1]], and \
    [[1, 2, 3], [1, 3, 2], [2, 1, 3],[2, 3, 1], [3, 1, 2], [3, 2, 1]]")
