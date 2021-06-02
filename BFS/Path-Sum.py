"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
"""


def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root == None:
        return False
    elif root.left == None and root.right == None and sum == root.val:
        return True
    return hasPathSum(root.left, sum - root.val) \
        or hasPathSum(root.right, sum - root.val)


print(hasPathSum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22))
print(hasPathSum([], 0))
print(hasPathSum([2, 3, 4, 10, None, 6, 4, 8, 5, None, 0, 1, 2], 35))
print("The booleans above should be True, False, and False.")
