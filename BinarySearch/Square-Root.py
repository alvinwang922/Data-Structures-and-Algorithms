"""
Implement int sqrt(int x). Compute and return the square root of x, 
where x is guaranteed to be a non-negative integer. Since the 
return type is an integer, the decimal digits are 
truncated and only the integer part of the result is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid
            else:
                left = mid + 1


print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(1))
print("The values above should be 2, 2, and 1.")
