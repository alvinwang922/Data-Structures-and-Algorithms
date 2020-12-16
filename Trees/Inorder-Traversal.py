"""
Given the root of a binary tree, return the inorder 
traversal of its nodes' values.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        ans, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans

    print(inorderTraversal([1, None, 2, 3]))
    print(inorderTraversal([1, 2]))
    print(inorderTraversal([1, 2, 3, 4, None, None, 6]))
    print("The arrays above should be[1, 3, 2], [2, 1], \
        and [4, 2, 1, 3, 6].")
