# Invert a binary tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root


print(invertTree([]))
print(invertTree([4, 2, 7, 1, 3, 6, 9]))
print(invertTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("The trees above should be None, [4, 7, 2, 9, 6, 3, 1], \
    and [1, 3, 2, 7, 6, 5, 4, null, null, null, null, null, 10, 9, 8].")
