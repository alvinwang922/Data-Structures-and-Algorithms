"""
Given the root node of a binary search tree, return the sum of 
values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int):
        if not root:
            return 0
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + \
            self.rangeSumBST(root.right, L, R)


print(rangeSumBST([10, 5, 15, 3, 7, null, 18], 7, 15))
print(rangeSumBST([10, 5, 15, 3, 7, 13, 18, 1, null, 6], 6, 10))
print(rangeSumBST([10, 5, 15, 4, 7, null, 18], 1, 3))
print("The values above should be 32, 23, and 0.")
