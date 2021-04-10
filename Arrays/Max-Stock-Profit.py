"""
Say you have an array prices for which the ith element
is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same
time (i.e., you must sell the stock before you buy again).
"""


def maxProfit(prices):
    i = 0
    localMin = prices[0]
    localMax = prices[0]
    maxProfit = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        localMin = prices[i]
        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        localMax = prices[i]
        maxProfit += localMax - localMin
    return maxProfit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))
print("The values above should be 7, 4, and 0.")
