"""
Say you have an array prices for which the ith element is the 
price of a given stock on day i. Design an algorithm to find 
the maximum profit. You may complete as many transactions as 
you like (i.e., buy one and sell one share of the stock multiple 
times). Note: You may not engage in multiple transactions at 
the same time (i.e., you must sell the stock before you buy again).
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
            currMax = max(0, prices[i] - prices[i - 1])
            actualMax += currMax
        return actualMax


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))
print("The values above should be 7, 4, and 0.")
