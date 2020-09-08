"""
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this 
place forms a binary tree". It will automatically contact the 
police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without 
alerting the police.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode):
        res = self.helper(root)
        return max(res[0], res[1])

    def helper(self, root):
        res = [0, 0]
        if root == None:
            return res
        left = self.helper(root.left)
        right = self.helper(root.right)
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res


print(rob([3, 2, 3, None, 3, None, 1]))
print(rob([1, 2, 3, None, 4, None, 5]))
print(rob([3, 4, 5, 1, 3, None, 1]))
print("The values above should be 7, 10, and 9.")
