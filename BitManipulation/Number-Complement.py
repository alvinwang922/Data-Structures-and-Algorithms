"""
Given a positive integer num, output its complement number. The 
complement strategy is to flip the bits of its binary representation.
"""


class Solution:
    def findComplement(self, num: int):
        final = ""
        for bit in bin(num)[2:]:
            if bit == "0":
                final += "1"
            else:
                final += "0"
        return int(final, 2)


print(findComplement(5))
print(findComplement(1))
print(findComplement(10))
print("The numbers above should be 2, 0, and 5.")
