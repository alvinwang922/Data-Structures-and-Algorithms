"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode, low=float("-inf"), high=float("inf")):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.isValidBST(root.left, low, min(high, root.val)) \
            and self.isValidBST(root.right, max(low, root.val), high)


print(isValidBST([2, 1, 3]))
print(isValidBST([5, 1, 4, None, None, 3, 6]))
print(isValidBST([1]))
print("The booleans above should be True, False, and True.")
