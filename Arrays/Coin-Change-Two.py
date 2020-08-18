"""
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that 
amount. You may assume that you have infinite number of each kind of coin.
"""


class Solution:
    def change(self, amount: int, coins: List[int]):
        combinations = [0] * (amount + 1)
        combinations[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                combinations[i] += combinations[i - coin]
        return combinations[-1]


print(change(5, [1, 2, 5]))
print(change(3, [2]))
print(change(10, [10]))
print("The values above should be 4, 0, and 10.")
