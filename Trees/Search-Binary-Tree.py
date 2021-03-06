"""
Given the root node of a binary search tree (BST) and a 
value. You need to find the node in the BST that the 
node's value equals the given value. Return the subtree 
rooted with that node. If such node doesn't exist, 
you should return None.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int):
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None


"""
Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, 
since there is no node with value 5, we should return None.

Note that an empty tree is represented by None, therefore 
you would see the expected output (serialized tree format) 
as [], not none.
"""
