"""
Given a circular array C of integers represented by A, find the 
maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the 
beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.
length, and C[i+A.length] = C[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer 
A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], 
there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
"""


class Solution:
    def maxSubarraySumCircular(self, A: List[int]):
        step = 0
        negative = True
        for item in A:
            if item > 0:
                negative = False
                break
        if negative:
            return max(A)
        dpmax, dpmin = [0] * len(A), [0] * len(A)
        dpmax[0] = A[0]
        dpmin[0] = A[0]
        for i in range(len(A)):
            dpmax[i] = max(dpmax[i-1] + A[i], A[i])
            dpmin[i] = min(dpmin[i-1] + A[i], A[i])
        return max(max(dpmax), sum(A) - min(dpmin))


print(maxSubarraySumCircular([1, -2, 3, -2]))
print(maxSubarraySumCircular([5, -3, 5]))
print(maxSubarraySumCircular([3, -1, 2, -1]))
print(maxSubarraySumCircular([3, -2, 2, -3]))
print(maxSubarraySumCircular([-2, -3, -1]))
print("The numbers above should be 3, 10, 4, 3, and -1.")
