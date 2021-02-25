"""
Given an array of integers nums and a positive integer k, find whether 
it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.
"""


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int):
        if len(nums) % k != 0:
            return False
        count = Counter(nums)
        keys = sorted(count.keys())
        for n in keys:
            if count[n] > 0:
                start = count[n]
                for i in range(n, n+k):
                    if count[i] < start:
                        return False
                    count[i] -= start
        return True

    print(isPossibleDivide([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
    print(isPossibleDivide([3, 3, 2, 2, 1, 1], 3))
    print(isPossibleDivide([1, 2, 3, 4], 3))
    print("The booleans above should be True, True, and False.")
