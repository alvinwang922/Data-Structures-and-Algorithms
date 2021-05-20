"""
Given a string containing digits from 2-9 inclusive, return 
all possible letter combinations that the number could 
represent. Return the answer in any order. A mapping of 
digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.
"""


def letterCombinations(digits: str):
    ans = []
    if not digits:
        return ans
    nums = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
    backtrack(digits, 0, "", nums, ans)
    return ans


def backtrack(digits, index, currString, nums, ans):
    if index == len(digits):
        ans.append(currString)
    else:
        for char in nums[digits[index]]:
            if index < len(digits):
                backtrack(digits, index + 1,
                          currString + char, nums, ans)


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
print("The arrays above should be [\"ad\",\"ae\",\"af\",\"bd\",\"be\",\
        \"bf\",\"cd\",\"ce\",\"cf\"], [], and [\"a\",\"b\",\"c\"].")
