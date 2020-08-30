"""

"""


class Solution:
    def divide(self, dividend: int, divisor: int):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


print(divide(10, 3))
print(divide(7, -3))
print(divide(4, 3))
print("The values above should be 3, -2, and 1.")
