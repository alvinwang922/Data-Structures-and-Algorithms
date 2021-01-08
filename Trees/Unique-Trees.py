"""
Given an integer n, generate all structurally unique 
BST's (binary search trees) that store values 1 ... n.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        if n < 1:
            return None
        return self.helper(1, n)

    def helper(self, start, end):
        nodes = []
        if start > end:
            nodes.append(None)
        for i in range(start, end + 1):
            leftNodes = self.helper(start, i - 1)
            rightNodes = self.helper(i + 1, end)
            for left in leftNodes:
                for right in rightNodes:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    nodes.append(root)
        return nodes


"""
Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique 
BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
