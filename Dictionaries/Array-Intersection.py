"""
Given two arrays, write a function to compute their intersection.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = defaultdict(int)
        ans = []
        for i in nums1:
            count[i] += 1
        for j in nums2:
            if j in count and count[j] > 0:
                ans.append(j)
                count[j] -= 1
        return ans


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersection([1, 3, 1], [2, 2]))
print("The arrays above should be [2], [9, 4], and [].")
