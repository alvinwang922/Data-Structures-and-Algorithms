"""
Convert a non-negative integer to its english words representation. 
Given input is guaranteed to be less than 2^31 - 1
"""


class Solution:
    def numberToWords(self, num: int):
        underTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six",
                       "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                       "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        if num == 0:
            return "Zero"
        english = ""
        for word in thousands:
            if num % 1000 != 0:
                english = self.breakDown(
                    num % 1000, underTwenty, tens, thousands) + word + " " + english
            num //= 1000
        return english.strip()

    def breakDown(self, num, underTwenty, tens, thousands):
        if num == 0:
            return ""
        elif num < 20:
            return underTwenty[num] + " "
        elif num < 100:
            return tens[num // 10] + " " + self.breakDown(num % 10, underTwenty, tens, thousands)
        else:
            return underTwenty[num // 100] + " Hundred " +
            self.breakDown(num % 100, underTwenty, tens, thousands)


print(numberToWords(123))
print(numberToWords(12345))
print(numberToWords(1234567))
print(numberToWords(1234567891))
print("The strings above should be \"One Hundred Twenty Three\", \"Twelve Thousand Three Hundred Forty Five\",\
     \"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven\", \
     and \"One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One\".")
