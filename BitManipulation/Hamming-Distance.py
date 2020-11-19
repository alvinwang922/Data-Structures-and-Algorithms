"""
The Hamming distance between two integers is the number of 
positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
"""


class Solution:
    def hammingDistance(self, x: int, y: int):
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y

    print(hammingDistance(1, 4))
    print(hammingDistance(2, 6))
    print(hammingDistance(63, 1))
    print("The values above should be 2, 1, and 5.")
