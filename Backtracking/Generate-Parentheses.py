"""
Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.
"""


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    backtrack(result, "", 0, 0, n * 2)
    return result


def backtrack(result, current, opening, closing, length):
    if len(current) == length:
        result.append(current)
        return result
    if opening < length // 2:
        backtrack(result, current + "(", opening + 1, closing, length)
    if closing < opening:
        backtrack(result, current + ")", opening, closing + 1, length)

    print(generateParenthesis(1))
    print(generateParenthesis(2))
    print(generateParenthesis(3))
    print("The arrays above should be ["()"], ["(())","()()"], and \
        ["((()))", "(()())", "(())()", "()(())", "()()()"].")
