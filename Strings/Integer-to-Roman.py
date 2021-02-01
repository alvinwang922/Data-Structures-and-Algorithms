"""
Convert an integer to a Roman numeral.
"""


class Solution:
    def intToRoman(self, num: int):
        ans = ""
        stack = []
        if num > 0:
            tempNum = num % 10
            if tempNum == 9:
                stack.append("IX")
            elif tempNum == 4:
                stack.append("IV")
            else:
                while tempNum > 5:
                    stack.append("I")
                    tempNum -= 1
                if tempNum == 5:
                    stack.append("V")
                    tempNum -= 5
                while tempNum:
                    stack.append("I")
                    tempNum -= 1
            num //= 10
        if num > 0:
            tempNum = num % 10
            if tempNum == 9:
                stack.append("XC")
            elif tempNum == 4:
                stack.append("XL")
            else:
                while tempNum > 5:
                    stack.append("X")
                    tempNum -= 1
                if tempNum == 5:
                    stack.append("L")
                    tempNum -= 5
                while tempNum:
                    stack.append("X")
                    tempNum -= 1
            num //= 10
        if num > 0:
            tempNum = num % 10
            if tempNum == 9:
                stack.append("CM")
            elif tempNum == 4:
                stack.append("CD")
            else:
                while tempNum > 5:
                    stack.append("C")
                    tempNum -= 1
                if tempNum == 5:
                    stack.append("D")
                    tempNum -= 5
                while tempNum:
                    stack.append("C")
                    tempNum -= 1
            num //= 10
        while num:
            stack.append("M")
            num -= 1
        while stack:
            ans += stack.pop()
        return ans


# Another solution
class Solution:
    def intToRoman(self, num: int):
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return thousands[num // 1000] + hundreds[(num % 1000) // 100] + \
            tens[(num % 100) // 10] + ones[num % 10]

    print(intToRoman(9))
    print(intToRoman(58))
    print(intToRoman(1994))
    print("The strings above should be \"IX\", \"LVIII\", and \"MCMXCIV\".")
