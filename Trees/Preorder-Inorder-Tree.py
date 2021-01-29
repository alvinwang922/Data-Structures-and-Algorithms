# Given preorder and inorder traversal of a tree, construct the binary tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        if inorder:
            rootIndex = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[rootIndex])
            root.left = self.buildTree(preorder, inorder[:rootIndex])
            root.right = self.buildTree(preorder, inorder[rootIndex + 1:])
            return root

    print(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
    print(buildTree([3, 9, 1, 2, 20, 15, 7], [1, 9, 2, 3, 15, 20, 7]))
    print("The trees above should be [3, 9, 20, null, null, 15, 7] \
        and [3, 9, 20, 1, 2, 15, 7].")
