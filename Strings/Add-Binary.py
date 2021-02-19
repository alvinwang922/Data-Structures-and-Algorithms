"""
Given two binary strings a and b, return their sum 
as a binary string.
"""


class Solution:
    def addBinary(self, a: str, b: str):
        carry = 0
        ans = ""
        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            ans += str(carry % 2)
            carry //= 2
        return ans[::-1]

    print(addBinary("11", "1"))
    print(addBinary("1010", "1011"))
    print("The strings above should be \"100\" and \
        \"10101\".")
