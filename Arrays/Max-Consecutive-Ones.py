"""
Given a binary array, find the maximum number of 
consecutive 1s in this array.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]):
        curr, ans = 0, 0
        for num in nums:
            if num == 1:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 0
        return ans

    print(findMaxConsecutiveOnes([0, 0]))
    print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(findMaxConsecutiveOnes([1, 0, 1]))
    print("The values above should be 0, 3, and 1.")
