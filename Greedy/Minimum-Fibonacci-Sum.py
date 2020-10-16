"""
Given an integer k, return the minimum number of Fibonacci numbers whose 
sum is equal to k. The same Fibonacci number can be used multiple times.
The Fibonacci numbers are defined as:
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 for n > 2.
It is guaranteed that for the given constraints we can always find such 
Fibonacci numbers that sum up to k.
"""


class Solution:
    def findMinFibonacciNumbers(self, k: int):
        ans, a, b = 0, 1, 1
        while b <= k:
            a, b = b, b + a
        while k > 0:
            if a <= k:
                k -= a
                ans += 1
            a, b = b - a, a
        return ans


print(findMinFibonacciNumbers(7))
print(findMinFibonacciNumbers(10))
print(findMinFibonacciNumbers(19))
print("The values above should be 2, 2, and 3.")
