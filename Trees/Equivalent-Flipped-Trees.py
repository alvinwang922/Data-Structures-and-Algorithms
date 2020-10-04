"""
For a binary tree T, we can define a flip operation as follows: 
choose any node, and swap the left and right child subtrees. A 
binary tree X is flip equivalent to a binary tree Y if and only 
if we can make X equal to Y after some number of flip operations. 
Given the roots of two binary trees root1 and root2, return true 
if the two trees are flip equivelent or false otherwise.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.flipEquiv(root1.left, root2.left) and \
            self.flipEquiv(root1.right, root2.right) or \
            self.flipEquiv(root1.left, root2.right) and \
            self.flipEquiv(root1.right, root2.left)


print(flipEquiv([1, 2, 3, 4, 5, 6, None, None, None, 7, 8],
                [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]))
print(flipEquiv([], []))
print(flipEquiv([0, None, 1], []))
print("The booleans above should be True, True, and False.")
