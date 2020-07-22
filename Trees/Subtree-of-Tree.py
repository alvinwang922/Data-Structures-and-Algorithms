"""
Given two non-empty binary trees s and t, check whether tree t has exactly 
the same structure and node values with a subtree of s. A subtree of s is 
a tree consists of a node in s and all of this node's descendants. The tree 
s could also be considered as a subtree of itself.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.compare(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def compare(self, s, t):
        if s and t:
            return s.val == t.val and self.compare(s.left, t.left) and self.compare(s.right, t.right)
        return s is t


print(isSubtree([3, 4, 5, 1, 2], [4, 1, 2]))
print(isSubtree([3, 4, 5, 1, 2], [4, 2, 2]))
print(isSubtree([], [4, 1, 2]))
print("The booleans above should be True, False, and False.")
