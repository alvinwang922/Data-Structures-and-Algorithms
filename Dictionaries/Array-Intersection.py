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
        ans = []
        freq = defaultdict(int)
        for i in range(len(nums1)):
            freq[nums1[i]] += 1
        for i in range(len(nums2)):
            if freq[nums2[i]] > 0 and nums2[i] not in ans:
                ans.append(nums2[i])
        return ans

    def main():
        print(intersection([1, 2, 2, 1], [2, 2]))
        print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
        print(intersection([1, 3, 1], [2, 2]))
        print("The arrays above should be [2], [9, 4], and [].")


# A shorter solution
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

    def main():
        print(intersection([1, 2, 2, 1], [2, 2]))
        print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
        print(intersection([1, 3, 1], [2, 2]))
        print("The arrays above should be [2], [9, 4], and [].")
