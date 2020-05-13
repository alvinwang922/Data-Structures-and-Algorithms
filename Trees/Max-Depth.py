# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along
# the longest path from the root node down to
# the farthest leaf node.
# Note: A leaf is a node with no children.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


print(maxDepth([3, 9, 20, null, null, 15, 7]))
print(maxDepth([]))
print(maxDepth([1, 2, 3, 4, 5, 6, 7, 8]))
print("The values above should be 3, 0, and 4.")
