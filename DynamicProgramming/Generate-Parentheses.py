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
        result = []
        self.backtrack(result, "", 0, 0, n * 2)
        return result

    def backtrack(self, result, current, opening, closing, length):
        if len(current) == length:
            result.append(current)
            return result
        if opening < length // 2:
            self.backtrack(result, current + "(", opening+1, closing, length)
        if closing < opening:
            self.backtrack(result, current + ")", opening, closing + 1, length)

    def main():
        print(generateParenthesis(1))
        print(generateParenthesis(2))
        print(generateParenthesis(3))
        print("The arrays above should be ["()"], ["(())","()()"], and \
            ["((()))", "(()())", "(())()", "()(())", "()()()"].")
