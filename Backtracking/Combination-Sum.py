"""
Given a set of candidate numbers (candidates) (without duplicates) 
and a target number (target), find all unique combinations in candidates
where the candidate numbers sums to target. The same repeated number may 
be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(candidates, [], target, res)
        return res
    
    def backtrack(self, candidates, combination, target, res):
        if target == 0:
            res.append(combination)
        else:
            for i in range(len(candidates)):
                if target > 0:
                    self.backtrack(candidates[i:], combination + [candidates[i]], \
                    target - candidates[i], res)


print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
print("The arrays above should be [[2, 2, 3], [7]] and [[2, 2, 2, 2], [2, 3, 3], [3, 5]]."