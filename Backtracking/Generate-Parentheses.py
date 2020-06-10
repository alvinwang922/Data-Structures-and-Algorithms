"""
Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j]
                          for y in dp[i - j - 1]]
        return dp[n]

    def main():
        print(generateParenthesis(1))
        print(generateParenthesis(2))
        print(generateParenthesis(3))
        print("The arrays above should be ["()"], ["(())","()()"], and \
            ["((()))", "(()())", "(())()", "()(())", "()()()"].")
