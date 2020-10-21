"""
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, also in sorted 
non-decreasing order.
"""


class Solution:
    def sortedSquares(self, A: List[int]):
        left, right = 0, len(A) - 1
        ans = [0] * len(A)
        while left <= right:
            A[left], A[right] = abs(A[left]), abs(A[right])
            if A[left] > A[right]:
                ans[right - left] = A[left] ** 2
                left += 1
            else:
                ans[right - left] = A[right] ** 2
                right -= 1
        return ans


print(sortedSquares([-4, -1, 0, 3, 10]))
print(sortedSquares([-7, -3, 2, 3, 11]))
print(sortedSquares([-8, -4, 0, 4, 9]))
print("The arrays above should be [0, 1, 9, 16, 100], \
    [4, 9, 9, 49, 121], and [0, 16, 16, 64, 81].")
