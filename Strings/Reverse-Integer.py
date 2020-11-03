"""
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment that could only 
store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, assume 
that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int):
        ans = int(str(abs(x))[::-1])
        return (-ans if x < 0 else ans) if ans.bit_length() < 32 else 0


print(reverse(-123))
print(reverse(120))
print(reverse(0))
print("The values above should be -321, 21, and 0.")
