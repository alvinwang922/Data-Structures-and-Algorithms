"""
A conveyor belt has packages that must be shipped from one port to 
another within D days. The i-th package on the conveyor belt has a 
weight of weights[i].  Each day, we load the ship with packages on 
the conveyor belt (in the order given by weights). We may not load 
more weight than the maximum weight capacity of the ship. Return 
the least weight capacity of the ship that will result in all the 
packages on the conveyor belt being shipped within D days.
"""


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (right + left) // 2
            currSum, days = 0, 1
            for weight in weights:
                if currSum + weight > mid:
                    currSum = 0
                    days += 1
                currSum += weight
            if days > D:
                left = mid + 1
            else:
                right = mid
        return left


print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(shipWithinDays([3, 2, 2, 4, 1, 4], 3))
print(shipWithinDays([1, 2, 3, 1, 1], 4))
print("The values above should be 15, 6, and 3.")
