"""
Given an array where elements are sorted in ascending order, convert it 
to a height balanced BST. For this problem, a height-balanced binary tree 
is defined as a binary tree in which the depth of the two subtrees 
of every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.insertNodes(nums)

    def insertNodes(self, nums):
        if len(nums) == 0:
            return
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.insertNodes(nums[0:mid])
        node.right = self.insertNodes(nums[mid + 1:])
        return node


print(sortedArrayToBST([-10, -3, 0, 5, 9]))
print(sortedArrayToBST([0, 1, 2, 3, 4, 5]))
print(sortedArrayToBST([]])
print(
    "The trees above should be [0,-3,9,-10,null,5], [3,1,5,0,2,4], and None.")
