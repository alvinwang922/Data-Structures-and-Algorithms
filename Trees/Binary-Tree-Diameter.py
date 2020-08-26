"""
Given a binary tree, you need to compute the length of the diameter 
of the tree. The diameter of a binary tree is the length of the 
longest path between any two nodes in a tree. This path may or 
may not pass through the root.
"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode):
        self.diameter = 0
        self.length(root)
        return self.diameter

    def length(self, root):
        if root:
            left = self.length(root.left)
            right = self.length(root.right)
            path = left + right
            if path > self.diameter:
                self.diameter = path
            return max(left, right) + 1
        return 0


print(diameterOfBinaryTree([1, 2, 3, 4, 5]))
print(diameterOfBinaryTree([1, 2, 3, 4, 5, 6, 7]))
print(diameterOfBinaryTree([1]))
print("The values above should be 3, 4, and 0.")
