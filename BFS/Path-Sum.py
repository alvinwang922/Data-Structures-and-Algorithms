"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
"""


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        elif root.left == None and root.right == None and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum - root.val) \
            or self.hasPathSum(root.right, sum - root.val)


print(hasPathSum([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], 22))
print(hasPathSum([], 0))
print(hasPathSum([2, 3, 4, 10, null, 6, 4, 8, 5, null, 0, 1, 2], 35))
print("The booleans above should be True, False, and False.")
