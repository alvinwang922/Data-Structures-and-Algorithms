"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous 
row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
Given row N and index K, return the K-th indexed symbol in row N. (The values 
of K are 1-indexed.) (1 indexed).
"""


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            if K == 1:
                return 0
            else:
                return 1
        half = 2 ** (N - 2)
        if K <= half:
            return self.kthGrammar(N - 1, K)
        else:
            res = self.kthGrammar(N - 1, K - half)
            if res == 0:
                return 1
            else:
                return 0


print(kthGrammar(1, 1))
print(kthGrammar(2, 1))
print(kthGrammar(2, 2))
print(kthGrammar(4, 5))
print("The values above should be 0, 0, 1, and 1.")
