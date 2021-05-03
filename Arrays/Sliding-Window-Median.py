"""
Median is the middle value in an ordered integer list. If the size 
of the list is even, there is no middle value. So the median is 
the mean of the two middle value. Given an array nums, there is a 
sliding window of size k which is moving from the very left of the 
array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. Your job 
is to output the median array for each window in the original array.
"""


from sortedcontainers import SortedList


def medianSlidingWindow(nums: List[int], k: int):
    window = SortedList()
    tracker, ans = 0, []
    for i in range(len(nums)):
        window.add(nums[i])
        if i - tracker + 1 == k:
            ans.append(self.median(window, k))
            window.remove(nums[tracker])
            tracker += 1
    return ans


def median(self, window, k):
    return window[k // 2] if (k % 2) \
        else (window[(k // 2) - 1] + window[k // 2]) / 2


print(medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 6))
print("The arrays above should be [1.00000, -1.00000, -1.00000, \
    3.00000, 5.00000, 6.00000] and [2.00000, 3.00000, 4.00000].")
