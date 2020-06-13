"""
Given a binary tree, return the level order traversal of its nodes'
values. (ie, from left to right, level by level).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        depth = self.maxDepth(root)
        res = [[] for i in range(depth)]
        self.levelOrderHelper(res, 0, root)
        return res

    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def levelOrderHelper(self, res, counter, root):
        if root is None:
            return
        res[counter].append(root.val)
        self.levelOrderHelper(res, counter + 1, root.left)
        self.levelOrderHelper(res, counter + 1, root.right)


print(levelOrder([3, 9, 20, null, null, 15, 7]))
print(levelOrder([]))
print(levelOrder([1, 2, 3]))
print("The arrays above should be [[3], [9, 20], [15, 7]], [], and [[1], [2, 3]]."
