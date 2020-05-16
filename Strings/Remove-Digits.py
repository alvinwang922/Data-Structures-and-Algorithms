# Given a non-negative integer num represented as a string,
# remove k digits from the number so that the new number
# is the smallest possible.
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.


class Solution(object):
    def removeKdigits(self, num, k):
        finalDigits = []
        counter = 0
        n = len(num)
        if n == k:
            return "0"
        for i in range(n):
            while k and finalDigits and finalDigits[-1] > num[i]:
                finalDigits.pop()
                k -= 1
            finalDigits.append(num[i])
        while k:
            finalDigits.pop()
            k -= 1
        return "".join(finalDigits).lstrip('0') or "0"


print(removeKdigits("1432219", 3))
print(removeKdigits("10200", 1))
print(removeKdigits("10", 2))
print("The values above should be \"1219\", \"200\", and \"0\".")
