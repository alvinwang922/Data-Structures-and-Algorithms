# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


class Solution(object):
    def climbStairs(self, n):
        if n < 4:
            return n
        stepsNeeded = [0] * n
        stepsNeeded[0] = 1
        stepsNeeded[1] = 2
        stepsNeeded[2] = 3
        for i in range(3, n):
            stepsNeeded[i] = stepsNeeded[i-1] + stepsNeeded[i-2]
        return stepsNeeded[n-1]


print(climbStairs(2))
print(climbStairs(5))
print(climbStairs(7))
print("The values above should be 2, 8, and 21.")
