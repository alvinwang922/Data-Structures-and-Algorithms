"""
Given a binary tree, find its minimum depth. The minimum depth is the number 
of nodes along the shortest path from the root node down to the nearest leaf 
node. Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def main():
        print(minDepth([3, 9, 20, None, None, 15, 7]))
        print(minDepth([1, 2]))
        print(minDepth([None]))
        print("The values above should be 2, 2, and 0.")
