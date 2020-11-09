"""
Given a binary tree, check whether it is a mirror of 
itself (ie, symmetric around its center).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val == right.val:
            return self.helper(left.left, right.right) and \
                self.helper(right.left, left.right)
        else:
            return False

    print(isSymmetric([]))
    print(isSymmetric([1, 2, 2, 3, 4, 4, 3]))
    print(isSymmetric([1, 2, 2, None, 3, None, 3]))
    print("The booleans above should be True, True, and False.")
