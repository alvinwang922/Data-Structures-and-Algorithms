"""
Write a function that takes an unsigned integer and 
returns the number of '1' bits it has (also known 
as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int):
        ans = 0
        while n:
            if n & 1:
                ans += 1
            n = n >> 1
        return ans

    print(hammingWeight(00000000000000000000000000001011))
    print(hammingWeight(00000000000000000000000010000000))
    print(hammingWeight(11111111111111111111111111111101))
    print("The values above should be 3, 1, and 31.")
