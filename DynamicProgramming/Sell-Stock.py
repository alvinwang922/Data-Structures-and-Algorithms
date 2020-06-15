"""
Say you have an array for which the ith element is the price of a given 
stock on day i. If you were only permitted to complete at most one 
transaction (i.e., buy one and sell one share of the stock), design 
an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.'
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        currMax = 0
        actualMax = 0
        for i in range(1, len(prices)):
            currMax = max(0, currMax + prices[i] - prices[i - 1])
            actualMax = max(currMax, actualMax)
        return actualMax


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([0]))
print("The values above should be 5, 0, and 0.")
