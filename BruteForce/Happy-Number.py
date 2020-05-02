# Write an algorithm to determine if a number n is "happy".
# A happy number is a number defined by the following
# process: Starting with any positive integer, replace
# the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1
# (where it will stay), or it loops endlessly in a
# cycle which does not include 1. Those numbers for
# which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.


class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            x = n
            n = 0
            while x > 0:
                n += (x % 10)*(x % 10)
                x = x // 10
        return n not in seen


print(isHappy(7))
print(isHappy(19))
print(isHappy(21))
print("The array above should be True, True, and False.")
