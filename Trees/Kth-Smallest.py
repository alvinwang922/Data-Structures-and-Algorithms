"""
Given a binary search tree, write a function kthSmallest to find 
the kth smallest element in it.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        return self.toList(root)[k - 1]

    def toList(self, root):
        nodes = []
        if root:
            leftNodes = self.toList(root.left)
            rightNodes = self.toList(root.right)
            nodes = leftNodes + [root.val] + rightNodes
        return nodes

    # another way to convert to list
    def toList2(self, root, nodes):
        if not root:
            return
        self.toList2(root.left, nodes)
        nodes.append(root.val)
        self.toList2(root.right, nodes)


print(KthSmallest([3, 1, 4, None, 2], 1))
print(KthSmallest([5, 3, 6, 2, 4, None, None, 1], 3))
print(KthSmallest([3, 2, 4], 3))
print("The values above should be 1, 3, and 4.")
