# Given a positive integer num, write a function which returns
# True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.


class Solution(object):
    def isPerfectSquare(self, num):
        addFactor = 3
        sum = 1
        while sum <= num:
            if sum == num:
                return True
            sum += addFactor
            addFactor += 2
        return False


print(isPerfectSquare(16))
print(isPerfectSquare(100))
print(isPerfectSquare(14))
print("The values above should be True, True, and False.")
