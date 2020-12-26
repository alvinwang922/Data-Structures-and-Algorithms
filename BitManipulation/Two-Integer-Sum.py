"""
Calculate the sum of two positive integers a and b,
but you are not allowed to use the operator + and -
"""


class Solution(object):
    def getSum(self, a, b):
        if (a == 0):
            return b
        carry = (a & b) << 1
        currSum = a ^ b
        return self.getSum(carry, currSum)

    print(getSum(2, 3))
    print(getSum(10, 13))
    print(getSum(20, 2))
    print("The values above should be 5, 23, 22.")
