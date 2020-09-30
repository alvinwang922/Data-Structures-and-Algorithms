"""
Let's call any (contiguous) subarray B (of A) a mountain if the following 
properties hold: B.length >= 3. There exists some 0 < i < B.length - 1 
such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)
Given an array A of integers, return the length of the longest mountain. 
Return 0 if there is no mountain.
"""


class Solution:
    def longestMountain(self, A: List[int]):
        start, mid, end, ans = 0, 0, 0, 0
        while start < len(A) - 1:
            while start < len(A) - 1 and A[start + 1] < A[start]:
                start += 1
            mid = start
            while mid < len(A) - 1 and A[mid + 1] > A[mid]:
                mid += 1
            end = mid
            while end < len(A) - 1 and A[end + 1] < A[end]:
                end += 1
            if end != mid and mid != start:
                ans = max(ans, end - start + 1)
                print(start, end, ans)
                start = end
            else:
                start = end + 1
        return ans


print(longestMountain([2, 1, 4, 7, 3, 2, 5]))
print(longestMountain([2, 2, 2]))
print(longestMountain([2, 3, 4]))
print("The values above should be 5, 0, and 0.")
