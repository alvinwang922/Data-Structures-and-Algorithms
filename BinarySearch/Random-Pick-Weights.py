"""
You are given an array of positive integers w where w[i] 
describes the weight of ith index (0-indexed). We need to 
call the function pickIndex() which randomly returns an 
integer in the range [0, w.length - 1]. pickIndex() should 
return the integer proportional to its weight in the w array.
"""


class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w

    def pickIndex(self):
        val = random.randrange(1, self.w[-1] + 1)
        l = 0
        r = len(self.w) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.w[mid] < val:
                l = mid + 1
            else:
                r = mid
        return l


"""
For example, for w = [1, 3], the probability of picking the 
index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability 
of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%). More 
formally, the probability of picking index i is w[i] / sum(w).
"""
