# Given a collection of distinct integers, return all possible permutations.


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, permutations, res):
        if not nums:
            res.append(permutations)
        else:
            for i in xrange(len(nums)):
                self.backtrack(nums[:i] + nums[i+1:],
                               permutations + [nums[i]], res)


print(permute([1, 2]))
print(permute([1, 2, 3]))
print(permute([]))
print("The arrays above should be [], [[1, 2], [2, 1]], and \
    [[1, 2, 3], [1, 3, 2], [2, 1, 3],[2, 3, 1], [3, 1, 2], [3, 2, 1]]")
