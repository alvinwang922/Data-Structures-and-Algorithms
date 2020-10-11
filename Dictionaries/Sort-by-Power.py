"""
The power of an integer x is defined as the number of steps 
needed to transform x into 1 using the following steps:
if x is even then x = x / 2
if x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps 
to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
Given three integers lo, hi and k. The task is to sort all 
integers in the interval [lo, hi] by the power value in 
ascending order, if two or more integers have the same power 
value sort them by ascending order. Return the k-th integer 
in the range [lo, hi] sorted by the power value.
Notice that for any integer x (lo <= x <= hi) it is guaranteed 
that x will transform into 1 using these steps and that the power 
of x is will fit in 32 bit signed integer.
"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int):
        powers = defaultdict()
        for i in range(lo, hi + 1):
            count = 0
            x = i
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                count += 1
            powers[i] = count
        sort = sorted(powers.items(), key=lambda x: x[1])
        return sort[k-1][0]


print(getKth(12, 15, 2))
print(getKth(7, 11, 4))
print(getKth(1, 1000, 777))
print("The values above should be 13, 7, and 570.")
