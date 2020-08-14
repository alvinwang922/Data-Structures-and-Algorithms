"""
We write the integers of A and B (in the order they are given) on two 
separate horizontal lines.
Now, we may draw connecting lines: a straight line connecting two 
numbers A[i] and B[j] such that:
A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number 
can only belong to one connecting line.
Return the maximum number of connecting lines we can draw in this way.
"""


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]):
        a, b = len(A), len(B)
        dp = [0] * (b + 1)
        for i in range(a):
            for j in range(b)[::-1]:
                if A[i] == B[j]:
                    dp[j + 1] = dp[j] + 1
            for j in range(b):
                dp[j + 1] = max(dp[j + 1], dp[j])
        return dp[b]


print(maxUncrossedLines([1, 4, 2], [1, 2, 4]))
print(maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
print(maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
print("The values above should be 2, 3, and 2.")
