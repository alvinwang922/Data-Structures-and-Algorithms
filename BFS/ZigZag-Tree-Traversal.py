"""
Given a binary tree, return the zigzag level order traversal of its 
nodes' values. (ie, from left to right, then right to left for 
the next level and alternate between).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        queue = [root]
        res = []
        tracker = 1
        while queue:
            temp = []
            for _ in range(len(queue)):
                tempNode = queue.pop(0)
                temp.append(tempNode.val)
                if tempNode.left:
                    queue.append(tempNode.left)
                if tempNode.right:
                    queue.append(tempNode.right)
            res.append(temp[::tracker])
            tracker *= -1
        return res


print(zigzagLevelOrder([3, 9, 20, None, None, 15, 7]))
print(zigzagLevelOrder([1, 2, 3, 4, 5, 6, 7]))
print(zigzagLevelOrder([]))
print("The arrays above should be [[3], [20, 9], [15, 7]], \
    [[1], [3, 2], [4, 5, 6, 7]], and None.")
