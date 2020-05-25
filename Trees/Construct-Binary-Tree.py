"""
Return the root node of a binary search tree that matches
the given preorder traversal. (Recall that a binary search
tree is a binary tree where for every node, any descendant
of node.left has a value < node.val, and any descendant of
node.right has a value > node.val.  Also recall that a preorder
traversal displays the value of the node first, then traverses
node.left, then traverses node.right.) It's guaranteed that for
the given test cases there is always possible to find a binary
search tree with the given requirements.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        s = []
        s.append(root)
        i = 1
        while (i < len(preorder)):
            temp = None
            while (len(s) > 0 and preorder[i] > s[-1].val):
                temp = s.pop()
            if (temp != None):
                temp.right = TreeNode(preorder[i])
                s.append(temp.right)
            else:
                temp = s[-1]
                temp.left = TreeNode(preorder[i])
                s.append(temp.left)
            i += 1
        return root


print(bstFromPreorder([8, 5, 1, 7, 10, 12])
print("Output should be [8,5,10,1,7,None,12]")
print(bstFromPreorder([1])
print("Output should be [1]")
print(bstFromPreorder([1, 2, 3])
print("Output should be [1,None,2,None,3]")
