"""
Given a collection of numbers, nums, that might contain duplicates, return all 
possible unique permutations in any order.
"""


def permuteUnique(self, nums):
    permutations = [[]]
    for first in nums:
        permutations = [rest[:i]+[first]+rest[i:] for rest in permutations
                        for i in range((rest+[first]).index(first)+1)]
    return permutations


print(permuteUnique([1, 1, 2]))
print(permuteUnique([1, 2, 3]))
print("The arrays above should be [[1,1,2], [1,2,1], [2,1,1]] and \
    [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]].")
