"""
Given two sorted integer arrays nums1 and nums2, merge nums2 
into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are 
m and n respectively. You may assume that nums1 has enough 
space (size that is equal to m + n) to hold additional 
elements from nums2.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        while n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        return nums1

    print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(merge([1, 2, 0, 0, 0], 2, [3, 5, 6], 3))
    print(merge([7, 9, 0, 0, 0], 2, [3, 5, 6], 3))
    print("The arrays above should be [1, 2, 2, 3, 5, 6], \
        [1, 2, 3, 5, 6], and [3, 5, 6, 7, 9].")
