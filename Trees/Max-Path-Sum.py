"""
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from 
some starting node to any node in the tree along the parent-child 
connections. The path must contain at least one node and does not 
need to go through the root.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode):
        sums = []
        self.getMaxSum(root, sums)
        return max(sums)

    def getMaxSum(self, root, sums):
        if not root:
            return 0
        left = max(self.getMaxSum(root.left, sums), 0)
        right = max(self.getMaxSum(root.right, sums), 0)
        currMax = root.val + left + right
        sums.append(currMax)
        return root.val + max(left, right)

    print(maxPathSum([1, 2, 3]))
    print(maxPathSum([-10, 9, 20, None, None, 15, 7]))
    print(maxPathSum([1, 2, None, 3, None, 4, None, 5]))
    print("The integers above should be 6, 42, 15.")
