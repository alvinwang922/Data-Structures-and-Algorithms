"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) 
of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes p and q as the lowest node in T that has both 
p and q as descendants (where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root
        return None


print(lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8))
print(lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4))
print(lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 7, 9))
print("The nodes above should have values 6, 2, and 6.")
