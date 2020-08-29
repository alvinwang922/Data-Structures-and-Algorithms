"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters 
as necessary until the first non-whitespace character is 
found. Then, starting from this character, takes an optional 
initial plus or minus sign followed by as many numerical 
digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that 
form the integral number, which are ignored and have no effect 
on the behavior of this function.
If the first sequence of non-whitespace characters in str is not 
a valid integral number, or if no such sequence exists because 
either str is empty or it contains only whitespace characters, 
no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, 
INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""


class Solution:
    def myAtoi(self, str: str):
        if not str:
            return 0
        negative = False
        str = str.strip()
        start = 0
        if start < len(str) and str[start] == "-":
            negative = True
            start += 1
        elif start < len(str) and str[start] == "+":
            start += 1
        end = start
        while end < len(str) and str[end].isnumeric():
            end += 1
        if start == end:
            return 0
        if negative:
            return max(int(str[start:end]) * -1, -2147483648)
        return min(int(str[start:end]), 2147483647)


print(myAtoi("42"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print("The values above should be 42, -42, 4193, and 0.")
