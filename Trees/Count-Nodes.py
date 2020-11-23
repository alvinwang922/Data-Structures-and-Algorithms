"""
Given a complete binary tree, count the number of nodes.
Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the 
last, is completely filled, and all nodes in the last level 
are as far left as possible. It can have between 1 and 2h 
nodes inclusive at the last level h.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode):
        if not root:
            return 0
        final = []
        self.helper(root, final)
        return len(final)

    def helper(self, root, final):
        final.append(root.val)
        if root.left:
            self.helper(root.left, final)
        if root.right:
            self.helper(root.right, final)

    # Another solution
    def countNodes2(self, root: TreeNode):
        if not root:
            return 0
        else:
            return 1 + self.countNodes(root.left) \
                + self.countNodes(root.right)

    # Another solution
    def countNodes3(self, root: TreeNode):
        if not root:
            return 0

        def dfs(root):
            if root.left and root.right:
                return dfs(root.left) + dfs(root.right) + 2
            elif root.left:
                return dfs(root.left) + 1
            else:
                return 0
        return dfs(root) + 1

    print(countNodes([1, 2, 3]))
    print(countNodes([1, 2, 3, 4, 5, 6]))
    print(countNodes([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("The values above should be 3, 6, and 9.")
