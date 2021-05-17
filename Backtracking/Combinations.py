"""
Given two integers n and k, return all possible combinations of 
k numbers out of 1 ... n. You may return the answer in any order.
"""


def combine(n: int, k: int):
    ans = []
    backtrack(n, k, [], 1, ans)
    return ans


def backtrack(n, k, curr, ind, ans):
    if len(curr) == k:
        ans.append(curr)
    else:
        for i in range(ind, n + 1):
            backtrack(n, k, curr + [i], i + 1, ans)


print(combine(4, 2))
print(combine(1, 1))
print("The arrays above should be [[1, 2], [1, 3], [1, 4], \
    [2, 3], [2, 4], [3, 4]] and [[1]].")
