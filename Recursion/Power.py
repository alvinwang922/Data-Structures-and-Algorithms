"""
Implement pow(x, n), which calculates x raised to the power n (x^n).
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            if n % 2 == 0:
                return self.myPow(x*x, n//2)
            else:
                return x * self.myPow(x*x, n//2)


print(myPow(2.00000, 10))
print(myPow(2.10000, 3))
print(myPow(2.00000, -2))
print("The values above should be 1024.00000, 9.26100, and 0.25.")
