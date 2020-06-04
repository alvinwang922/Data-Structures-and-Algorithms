"""
You are given two integer arrays nums1 and nums2 sorted in ascending order 
and an integer k. Define a pair (u,v) which consists of one element from 
the first array and one element from the second array. Find the k pairs 
(u1,v1),(u2,v2)...(uk,vk) with the smallest sums.
"""


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        visited = []
        heap = []
        answer = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.append((0, 0))

        while len(answer) < k and heap:

            val = heappop(heap)
            answer.append((nums1[val[1]], nums2[val[2]]))

            if val[1] + 1 < len(nums1) and (val[1] + 1, val[2]) not in visited:
                heappush(heap, (nums1[val[1] + 1] +
                                nums2[val[2]], val[1] + 1, val[2]))
                visited.append((val[1] + 1, val[2]))

            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heappush(heap, (nums1[val[1]] +
                                nums2[val[2] + 1], val[1], val[2] + 1))
                visited.append((val[1], val[2] + 1))

        return answer

    def main():
        print kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
        print kSmallestPairs([1, 1, 2], [1, 2, 3], 2)
        print kSmallestPairs([1, 2], [3], 3)
        print(
            "The arrays above should be [[1,2],[1,4],[1,6]], [1,1],[1,1], and [1,3],[2,3].")
