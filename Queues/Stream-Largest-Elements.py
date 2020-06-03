"""
Design a class to find the kth largest element in a stream. Note that it 
is the kth largest element in the sorted order, not the kth distinct element.
Your KthLargest class will have a constructor which accepts an integer k 
and an integer array nums, which contains initial elements from the stream. 
For each call to the method KthLargest.add, return the element representing 
the kth largest element in the stream.
"""


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        else:
            heapq.heappushpop(self.pool, val)
        return self.pool[0]

    def main():
        k = 3
        arr = [4, 5, 8, 2]
        kthLargest = KthLargest(3, arr)
        print(kthLargest.add(3))
        print(kthLargest.add(5))
        print(kthLargest.add(10))
        print(kthLargest.add(9))
        print(kthLargest.add(4))
        print("The values printed above should be 4, 5, 5, 8, and 8.")
