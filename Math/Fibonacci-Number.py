"""
The Fibonacci numbers, commonly denoted F(n) form 
a sequence, called the Fibonacci sequence, such 
that each number is the sum of the two preceding 
ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""


class Solution:
    def fib(self, n: int):
        if n <= 1:
            return n
        a, b = 0, 1
        while n > 1:
            curr = a + b
            a, b = b, curr
            n -= 1
        return b

    print(fib(2))
    print(fib(3))
    print(fib(4))
    print("The values above should be 1, 2, and 3.")
