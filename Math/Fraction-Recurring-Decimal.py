"""
Given two integers representing the numerator and denominator of a 
fraction, return the fraction in string format. If the fractional 
part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 
104 for all the given inputs.
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int):
        num, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ""
        ans = [sign + str(num), "."]
        remainders = {}
        while remainder > 0 and remainder not in remainders:
            remainders[remainder] = len(ans)
            num, remainder = divmod(remainder * 10, abs(denominator))
            ans.append(str(num))
        if remainder in remainders:
            ans.insert(remainders[remainder], '(')
            ans.append(')')
        return ''.join(ans).rstrip(".")

    print(fractionToDecimal(2, 1))
    print(fractionToDecimal(1, 5))
    print(fractionToDecimal(4, 333))
    print("The strings above should be \"2\", \"0.2\", and \"0.(012)\".")
