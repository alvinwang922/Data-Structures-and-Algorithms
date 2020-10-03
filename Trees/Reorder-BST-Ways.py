"""
Given an array nums that represents a permutation of integers from 1 to n. 
We are going to construct a binary search tree (BST) by inserting the 
elements of nums in order into an initially empty BST. Find the number of 
different ways to reorder nums so that the constructed BST is identical to 
that formed from the original array nums. For example, given nums = [2,1,3], 
we will have 2 as the root, 1 as a left child, and 3 as a right child. The 
array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is 
identical to the original BST formed from nums. Since the answer may be very 
large, return it modulo 10^9 + 7.
"""


class Solution:
    def numOfWays(self, nums: List[int]):
        memo = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]

        def combinations(x, y):
            if x == 0 or y == 0:
                return 1
            if memo[x][y] != -1:
                return memo[x][y]
            memo[x][y] = combinations(x, y - 1) + combinations(x - 1, y)
            return memo[x][y]

        def total(nums):
            if len(nums) <= 2:
                return 1
            left, right = [], []
            for i in range(1, len(nums)):
                if nums[i] < nums[0]:
                    left.append(nums[i])
                if nums[i] > nums[0]:
                    right.append(nums[i])
            count = combinations(len(left), len(right))
            return count * total(left) * total(right)

        return (total(nums) - 1) % (10 ** 9 + 7)


print(numOfWays([3, 4, 5, 1, 2]))
print(numOfWays([1, 2, 3]))
print(numOfWays([3, 1, 2, 5, 4, 6]))
print(numOfWays([9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18]))
print("The values above should be 5, 0, 19, and 216212978.")
