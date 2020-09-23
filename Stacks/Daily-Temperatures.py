"""
Given a list of daily temperatures T, return a list such that, for each day in 
the input, tells you how many days you would have to wait until a warmer 
temperature. If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].
Note: The length of temperatures will be in the range [1, 30000]. Each 
temperature will be an integer in the range [30, 100].
"""


class Solution:
    def dailyTemperatures(self, T: List[int]):
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans


print(dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperature([31, 32, 33, 34, 35]))
print(dailyTemperature([35, 34, 33, 32, 31]))
print("The lists above should be[1, 1, 4, 2, 1, 1, 0, 0], \
    [1, 1, 1, 1, 0], and [0, 0, 0, 0, 0].")
