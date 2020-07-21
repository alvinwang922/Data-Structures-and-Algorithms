"""
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later 
in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialized = []

        def toString(root):
            if root:
                serialized.append(str(root.val))
                toString(root.left)
                toString(root.right)
            else:
                serialized.append("None")
        toString(root)
        return " ".join(serialized)

    def deserialize(self, data):
        def toTree():
            nodeVal = next(nodes)
            if nodeVal == "None":
                return None
            node = TreeNode(int(nodeVal))
            node.left = toTree()
            node.right = toTree()
            return node
        nodes = iter(data.split())
        return toTree()
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """


codec = Codec()
root1 = [1, 2, 3, None, None, 4, 5]
root2 = [1, None, 3]
root3 = [1, 2, 3, None, 5, None, 6]
print(codec.deserialize(codec.serialize(root1)))
print(codec.deserialize(codec.serialize(root2)))
print(codec.deserialize(codec.serialize(root3)))
print("The trees above should be [1, 2, 3, None, None, 4, 5], [1, None, 3], \
    and [1, 2, 3, None, 5, None, 6].")
