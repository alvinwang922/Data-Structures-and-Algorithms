"""
Given a non negative integer number num. For every numbers i 
in the range 0 ≤ i ≤ num calculate the number of 1's in their 
binary representation and return them as an array.
"""


class Solution:
    def countBits(self, num: int):
        final = [0]
        while len(final) <= num:
            final += [i+1 for i in final]
        return final[:num+1]


print(countBits(2))
print(countBits(5))
print(countBits(7))
print("The arrays above should be [0, 1, 1], [0, 1, 1, 2, 1, 2], \
    and [0, 1, 1, 2, 1, 2, 2, 3].")
