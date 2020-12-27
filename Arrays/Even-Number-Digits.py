"""
Given an array nums of integers, return how many of them 
contain an even number of digits.
"""


class Solution:
    def findNumbers(self, nums: List[int]):
        return sum((len(str(num))) % 2 == 0 for num in nums)

    # Faster solution
    def findNumbers2(self, nums: List[int]):
        ans = 0
        for num in nums:
            if (10 <= num <= 99) or (1000 <= num <= 9999) \
                    or (num == 100000):
                ans += 1
        return ans

    print(findNumbers([1]))
    print(findNumbers([12, 345, 2, 6, 7896]))
    print(findNumbers([555, 901, 482, 1771]))
    print("The values above should be 0, 2, and 1.")
