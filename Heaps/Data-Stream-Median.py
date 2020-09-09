"""
Median is the middle value in an ordered integer list. If the size of the 
list is even, there is no middle value. So the median is the mean of the 
two middle value. For example, [2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data 
structure; double findMedian() - Return the median of all elements so far.
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low, self.high = [], []

    def addNum(self, num: int):
        if len(self.low) == len(self.high):
            heappush(self.high, -heappushpop(self.low, -num))
        else:
            heappush(self.low, -heappushpop(self.high, num))

    def findMedian(self):
        if len(self.low) == len(self.high):
            return (self.high[0] - self.low[0]) / 2
        else:
            return self.high[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""
