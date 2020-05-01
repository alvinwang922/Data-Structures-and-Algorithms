# You are given coins of different denominations
# and a total amount of money amount. Write a
# function to compute the fewest number of coins
# that you need to make up that amount. If that
# amount of money cannot be made up by any
# combination of the coins, return -1.


class Solution(object):
    def coinChange(self, coins, amount):
        # dp is the array with number of minimum
        # coins to make each index value
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]


print(coinChange([1, 2, 5], 11))
print(coinChange([2], 3))
print(coinChange([3, 7, 15], 28))
print("The array above should be 3, -1, and 4.")
