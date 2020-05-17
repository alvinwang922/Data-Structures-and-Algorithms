# Given two binary trees, write a function to
# check if they are the same or not.
# Two binary trees are considered the same if
# they are structurally identical and the
# nodes have the same value


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if p is not None and q is not None:
            if p.val == q.val and self.isSameTree(p.left, q.left) \
                    and self.isSameTree(p.right, q.right):
                return True
        return p == q


print(isSameTree([1, 2, 3], [1, 2, 3]))
print(isSameTree([1, 2], [1, None, 2]))
print(isSameTree([1, 2, 1], [1, 1, 2]))
print("The booleans above should be True, False, and False.")
