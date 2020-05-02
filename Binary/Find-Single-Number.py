# Given a non-empty array of integers, every
# element appears twice except for one.
# Find that single one.


class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)


print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([2, 2, 1]))
print(singleNumber([1, 2, 3, 1, 2, 3, 5]))
print("The array above should be 4, 1, and 5.")
