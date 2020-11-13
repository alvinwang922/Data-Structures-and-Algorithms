"""
Given a binary tree, write a function to get the maximum 
width of the given tree. The maximum width of a tree is 
the maximum width among all levels. The width of one 
level is defined as the length between the end-nodes 
(the leftmost and right most non-null nodes in the level, 
where the null nodes between the end-nodes are also counted 
into the length calculation. It is guaranteed that the 
answer will in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode):
        if not root:
            return []
        ans, curr = 0, [(root, 1)]
        while len(curr):
            ans = max(ans, curr[-1][1] - curr[0][1] + 1)
            after = []
            for node, index in curr:
                if node.left:
                    after.append((node.left, index * 2))
                if node.right:
                    after.append((node.right, index * 2 + 1))
            curr = after
        return ans

    print(widthOfBinaryTree([1, 3, 2, 5, 3, None, 9]))
    print(widthOfBinaryTree([1, 3, None, 5, 3]))
    print(widthOfBinaryTree([1, 3, 2, 5]))
    print("The values above should be 4, 2, and 2.")
