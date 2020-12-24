"""
Given an integer n, return the number of 
trailing zeroes in n!.
Follow up: Could you write a solution that 
works in logarithmic time complexity?
"""


class Solution:
    def trailingZeroes(self, n: int):
        ans, i = 0, 5
        while i <= n:
            ans += (n // i)
            i *= 5
        return ans

    # Recursive solution
    def trailingZeroes(self, n: int):
        if n == 0:
            return 0
        return n // 5 + \
            self.trailingZeroes(n // 5)

    print(trailingZeroes(3))
    print(trailingZeroes(5))
    print(trailingZeroes(321))
    print("The values above should be 0, 1, and 78.")
