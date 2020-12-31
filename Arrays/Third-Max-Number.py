"""
Given a non-empty array of integers, return the 
third maximum number in this array. If it does 
not exist, return the maximum number. The time 
complexity must be in O(n).
"""


class Solution:
    def thirdMax(self, nums: List[int]):
        first, second, third = -float("inf"), \
            -float("inf"), -float("inf")
        for num in nums:
            if num == first or num == second \
                    or num == third:
                continue
            if num > first:
                num, first = first, num
            if num > second:
                num, second = second, num
            if num > third:
                num, third = third, num
        if third == -float("inf"):
            return first
        else:
            return third

    print(thirdMax([3, 2, 1]))
    print(thirdMax([1, 2]))
    print(thirdMax([3, 4, 5, 6, 7]))
    print("The values above should be 1, 2, and 5.")
