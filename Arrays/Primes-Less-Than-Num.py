# Count the number of prime numbers less than a non-negative number, n.


class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        counter = 0
        nums = [True] * n
        nums[0] = False
        nums[1] = False
        for i in range(2, n):
            if nums[i] == True:
                counter += 1
                j = 2
                while i * j < n:
                    nums[i * j] = False
                    j += 1
        return counter


print(countPrimes(1))
print(countPrimes(3))
print(countPrimes(10))
print("The values above should be 0, 1, and 4.")
