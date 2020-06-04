"""
Given a non-empty array of integers, return the k most frequent elements.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = defaultdict(list)
        for key, count in Counter(nums).items():
            frequency[count].append(key)
        top = []
        for times in reversed(range(len(nums) + 1)):
            top.extend(frequency[times])
        return top[:k]

    def main():
        print topKFrequent([1, 1, 1, 2, 2, 3], 2)
        print topKFrequent([1], 1)
        print topKFrequent([1, 1, 1, 2, 2, 3], 3)
        print("The arrays above should be [1, 2], [1], and [1, 2, 3]")
