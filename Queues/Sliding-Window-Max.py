"""
Given an array nums, there is a sliding window of size k which 
is moving from the very left of the array to the very right. You 
can only see the k numbers in the window. Each time the sliding 
window moves right by one position. Return the max sliding window.
Follow up: Could you solve it in linear time?
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        q, res = deque(), []
        for i in range(len(nums)):
            if i - k >= 0:
                res.append(nums[q[0]])
                while q and q[0] <= i - k:
                    q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        return res


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(maxSlidingWindow([1, 3, 4, 2, 5, 7], 2))
print(maxSlidingWindow([1, 2, 4, 5, 9, 7], 4))
print("The arrays above should be [3, 3, 5, 5, 6, 7], \
    [3, 4, 4, 5, 7], and [5, 9, 9].")
