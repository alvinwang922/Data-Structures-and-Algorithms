"""
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the 
sorted order, not the kth distinct element.
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        nums.sort()
        return nums[-k]

    print(findKthLargest([1, 2, 3], 3))
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print("The values above should be 1, 4, and 5.")
