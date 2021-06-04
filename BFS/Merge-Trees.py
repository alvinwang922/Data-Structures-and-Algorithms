"""
Given two binary trees and imagine that when you put one of them to 
cover the other, some nodes of the two trees are overlapped while 
the others are not. You need to merge them into a new binary tree. 
The merge rule is that if two nodes overlap, then sum node values 
up as the new value of the merged node. Otherwise, the NOT null 
node will be used as the node of new tree.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(self, t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 and t2:
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    else:
        return t1 or t2


print(mergeTrees([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]))
print(mergeTrees([9, -1, None, -2, 0, -4, None, None, 8, -5, -3, 6,
                  None, None, None, None, None, None, 7],
                 [-1, -2, 0, None, None, None, 8, 6, None, None, 7]))
print(mergeTrees([1], []))
print("The trees above should be [3,4,5,5,4,None,7], \
    [8,-3,0,-2,0,None,8,-4,None,None,8,6,None,-5,-3,6,None,\
        None,7,None,None,None,None,None,7], and [1].")
